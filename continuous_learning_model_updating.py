import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
from tensorflow.keras.models import clone_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import logging
from datetime import datetime
import torch
from stable_baselines3 import PPO
from collections import deque

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContinuousLearningModelUpdating:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", lookback=60, ensemble_size=3):
        """
        مقداردهی اولیه ماژول بهینه‌سازی و یادگیری تطبیقی
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param lookback: تعداد کندل‌های گذشته
        :param ensemble_size: تعداد مدل‌ها در Ensemble
        """
        self.db_name = db_name
        self.symbol = symbol
        self.lookback = lookback
        self.ensemble_size = ensemble_size
        self.scaler = MinMaxScaler()

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")

        # بارگذاری مدل‌های اولیه از AI Trading Core (فرض بر اینه که این مدل‌ها از قبل ساخته شدن)
        from ai_trading_core import AITradingCore
        self.ai_core = AITradingCore(db_name, symbol, lookback)
        self.lstm_models = [clone_model(self.ai_core.lstm_model) for _ in range(ensemble_size)]
        self.transformer_models = [self.ai_core.build_transformer_model() for _ in range(ensemble_size)]
        self.ppo_model = self.ai_core.ppo_model

        # معیارهای عملکرد
        self.performance_metrics = {
            "win_rate": 0.0,
            "profit_factor": 0.0,
            "max_drawdown": 0.0,
            "sharpe_ratio": 0.0
        }
        self.trade_history = deque(maxlen=1000)  # تاریخچه معاملات

    # --- بارگذاری داده‌های جدید ---
    def load_new_data(self, table_name="realtime_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(
            f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}' ORDER BY time DESC LIMIT {self.lookback * 2}",
            conn)
        conn.close()
        if df.empty:
            logger.warning(f"جدول {table_name} برای {self.symbol} خالی است یا داده‌ای ندارد.")
        return df

    # --- بارگذاری داده‌های تاریخی ---
    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        if df.empty:
            logger.warning(f"جدول {table_name} برای {self.symbol} خالی است یا داده‌ای ندارد.")
        return df

    # --- به‌روزرسانی آنلاین مدل‌ها ---
    def update_models_online(self, df):
        """
        به‌روزرسانی تدریجی مدل‌های LSTM و Transformer با داده‌های جدید
        :param df: DataFrame داده‌های جدید
        """
        if df.empty:
            logger.warning("دیتافریم ورودی خالی است، به‌روزرسانی مدل‌ها لغو شد.")
            return

        if len(df) < self.lookback:
            logger.warning(f"تعداد کندل‌ها ({len(df)}) کمتر از lookback ({self.lookback}) است.")
            return

        # فقط آخرین داده‌های مورد نیاز رو نگه می‌داریم
        df = df.tail(self.lookback * 2)
        df_tech = self.ai_core.technical_analysis(df)
        if df_tech.empty:
            logger.warning("داده‌های کافی برای محاسبه اندیکاتورها وجود ندارد.")
            return

        X, y = self.ai_core.prepare_data_for_prediction(df_tech)
        if len(X) < 1:
            logger.warning("داده کافی برای به‌روزرسانی مدل موجود نیست.")
            return

        # به‌روزرسانی LSTM‌ها با بچ‌های کوچک‌تر
        batch_size = min(16, len(X))  # بچ سایز رو محدود می‌کنیم
        for i, model in enumerate(self.lstm_models):
            model.fit(X, y, epochs=1, batch_size=batch_size, verbose=0, shuffle=False)
            logger.info(f"مدل LSTM {i + 1} به‌روز شد.")
            del X, y  # آزاد کردن حافظه
            X, y = self.ai_core.prepare_data_for_prediction(df_tech)  # دوباره بارگذاری

        # به‌روزرسانی Transformer‌ها
        X_torch = torch.tensor(X, dtype=torch.float32)
        y_torch = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
        for i, model in enumerate(self.transformer_models):
            optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
            loss_fn = torch.nn.MSELoss()
            optimizer.zero_grad()
            pred = model(X_torch[:batch_size])  # فقط یه بچ پردازش می‌کنیم
            loss = loss_fn(pred, y_torch[:batch_size])
            loss.backward()
            optimizer.step()
            logger.info(f"مدل Transformer {i + 1} به‌روز شد.")

        # به‌روزرسانی PPO با تعداد کمتر timesteps
        self.ppo_model.learn(total_timesteps=500)  # کاهش از 1000 به 500
        logger.info("مدل PPO به‌روز شد.")
        del X_torch, y_torch  # آزاد کردن حافظه

    # --- پیش‌بینی با Ensemble ---
    def ensemble_predict(self, df):
        try:
            if len(df) < self.lookback:
                logger.warning(f"تعداد کندل‌ها ({len(df)}) کمتر از lookback ({self.lookback}) است.")
                return 0

            df_tech = self.ai_core.technical_analysis(df)
            if df_tech.empty or len(df_tech) < self.lookback:
                logger.warning(f"داده‌های کافی پس از تحلیل تکنیکال وجود ندارد (تعداد کندل‌ها: {len(df_tech)}).")
                return 0

            X, _ = self.ai_core.prepare_data_for_prediction(df_tech)
            if len(X) == 0:
                logger.warning("داده‌های آماده‌شده برای پیش‌بینی خالی است.")
                return 0

            # پیش‌بینی با مدل‌های LSTM
            lstm_preds = []
            for model in self.lstm_models:
                pred = model.predict(X[-1].reshape(1, self.lookback, 6), verbose=0)
                lstm_preds.append(np.mean(pred.flatten()))  # فلت کردن و میانگین‌گیری

            # پیش‌بینی با مدل‌های Transformer
            X_torch = torch.tensor(X[-1].reshape(1, self.lookback, 6), dtype=torch.float32)
            transformer_preds = []
            for model in self.transformer_models:
                pred = model(X_torch).detach().numpy()
                transformer_preds.append(np.mean(pred.flatten()))  # فلت کردن و میانگین‌گیری

            # پیش‌بینی با PPO
            state = self.ai_core._get_state(df_tech)  # حالا شکل (3,) داره
            ppo_pred = self.ppo_model.predict(state)[0]

            # ترکیب پیش‌بینی‌ها
            all_preds = lstm_preds + transformer_preds
            avg_pred = np.mean(all_preds)
            if ppo_pred == 1:
                final_pred = 1 if avg_pred > 0 else 0
            elif ppo_pred == 2:
                final_pred = -1 if avg_pred < 0 else 0
            else:
                final_pred = 1 if avg_pred > 0.5 else -1 if avg_pred < -0.5 else 0

            return final_pred
        except Exception as e:
            logger.error(f"خطا در پیش‌بینی ترکیبی: {e}")
            return 0

    # --- بک‌تست و Forward Testing ---
    def backtest_and_forward_test(self, historical_df, new_df):
        """
        ارزیابی عملکرد مدل با بک‌تست و Forward Testing
        :param historical_df: داده‌های تاریخی
        :param new_df: داده‌های جدید
        :return: معیارهای عملکرد
        """
        # پردازش دیتا
        historical_df_tech = self.ai_core.technical_analysis(historical_df)
        new_df_tech = self.ai_core.technical_analysis(new_df)

        if historical_df_tech.empty or new_df_tech.empty:
            logger.warning("داده‌های کافی برای بک‌تست یا Forward Testing وجود ندارد.")
            return self.performance_metrics

        # بک‌تست
        balance = 10000
        trades = []
        for i in range(self.lookback, len(historical_df_tech)):
            df_slice = historical_df_tech.iloc[i - self.lookback:i]
            signal = self.ensemble_predict(df_slice)
            next_price = historical_df_tech['close'].iloc[i]
            prev_price = historical_df_tech['close'].iloc[i - 1]
            profit = (next_price - prev_price) * 10 if signal == 1 else (
                                                                                    prev_price - next_price) * 10 if signal == -1 else 0
            balance += profit
            trades.append(profit)

        # Forward Testing
        forward_trades = []
        for i in range(self.lookback, len(new_df_tech)):
            df_slice = new_df_tech.iloc[i - self.lookback:i]
            signal = self.ensemble_predict(df_slice)
            next_price = new_df_tech['close'].iloc[i]
            prev_price = new_df_tech['close'].iloc[i - 1]
            profit = (next_price - prev_price) * 10 if signal == 1 else (
                                                                                    prev_price - next_price) * 10 if signal == -1 else 0
            forward_trades.append(profit)

        # محاسبه معیارها
        self.calculate_performance_metrics(trades + forward_trades)
        return self.performance_metrics

    # --- محاسبه معیارهای عملکرد ---
    def calculate_performance_metrics(self, trades):
        """
        محاسبه معیارهای عملکرد
        :param trades: لیست سود و ضرر معاملات
        """
        wins = [t for t in trades if t > 0]
        losses = [abs(t) for t in trades if t < 0]

        self.performance_metrics["win_rate"] = len(wins) / len(trades) if trades else 0
        self.performance_metrics["profit_factor"] = sum(wins) / sum(losses) if losses else float('inf')

        # محاسبه Maximum Drawdown
        balance = 10000
        peak = balance
        max_dd = 0
        for trade in trades:
            balance += trade
            peak = max(peak, balance)
            dd = (peak - balance) / peak
            max_dd = max(max_dd, dd)
        self.performance_metrics["max_drawdown"] = max_dd

        # محاسبه Sharpe Ratio (ساده‌سازی شده)
        returns = np.array(trades)
        self.performance_metrics["sharpe_ratio"] = returns.mean() / returns.std() if returns.std() != 0 else 0

        logger.info(f"معیارهای عملکرد: {self.performance_metrics}")

    # --- بهینه‌سازی مدل بر اساس معیارها ---
    def optimize_models(self):
        """
        بهینه‌سازی مدل‌ها بر اساس معیارهای عملکرد
        """
        if self.performance_metrics["win_rate"] < 0.5 or self.performance_metrics["max_drawdown"] > 0.2:
            logger.warning("عملکرد ضعیف تشخیص داده شد، بهینه‌سازی مدل‌ها...")
            # تنظیم مجدد وزن‌ها یا تغییر هایپرپارامترها
            for model in self.lstm_models:
                model.compile(optimizer='adam', loss='mse')  # بازنشانی بهینه‌ساز
            for model in self.transformer_models:
                for param in model.parameters():
                    param.data = param.data * 0.95  # کاهش اندک وزن‌ها
            self.ppo_model = PPO("MlpPolicy", self.ai_core.env, verbose=0)  # بازنشانی PPO

    # --- اجرای کامل ماژول ---
    def run(self):
        try:
            historical_df = self.load_data("historical_data")
            new_df = self.load_new_data("realtime_data")

            if historical_df.empty or len(historical_df) < self.lookback * 2:
                logger.warning("داده‌های تاریخی کافی نیست.")
                return {"win_rate": 0, "max_drawdown": 0, "profit_factor": 0, "sharpe_ratio": 0}

            self.update_models_online(historical_df.tail(self.lookback * 2))
            metrics = self.backtest_and_forward_test(historical_df.tail(self.lookback * 10), new_df)
            self.optimize_models()
            signal = self.ensemble_predict(historical_df.tail(self.lookback * 2))
            logger.info(f"سیگنال جدید پس از به‌روزرسانی: {signal}")
            return metrics
        except Exception as e:
            logger.error(f"خطا در اجرای ماژول یادگیری تطبیقی: {str(e)}")
            return {"win_rate": 0, "max_drawdown": 0, "profit_factor": 0, "sharpe_ratio": 0}

            self.update_models_online(data_to_use)
            historical_df = historical_df.tail(self.lookback * 10)
            new_df = new_df.tail(self.lookback * 2)
            metrics = self.backtest_and_forward_test(historical_df, new_df)
            self.optimize_models()
            signal = self.ensemble_predict(data_to_use)
            logger.info(f"سیگنال جدید پس از به‌روزرسانی: {signal}")
            return metrics
        except Exception as e:
            logger.error(f"خطا در اجرای ماژول یادگیری تطبیقی: {e}")
            return {"win_rate": 0, "max_drawdown": 0, "profit_factor": 0, "sharpe_ratio": 0}

if __name__ == "__main__":
    # نمونه اجرا
    learning_module = ContinuousLearningModelUpdating(db_name="trading_data.db", symbol="EURUSD_i", lookback=60,
                                                      ensemble_size=3)
    signal = learning_module.run()
    print(f"سیگنال نهایی: {signal}")
