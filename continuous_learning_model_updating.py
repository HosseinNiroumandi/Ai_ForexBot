import sqlite3
import pandas as pd
import numpy as np
import talib
import torch
import torch.nn as nn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import logging
from ai_trading_core import AITradingCore

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContinuousLearningModelUpdating:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", lookback=60, ensemble_size=3):
        self.db_name = db_name
        self.symbol = symbol
        self.lookback = lookback
        self.ensemble_size = ensemble_size
        self.ai_core = AITradingCore(db_name=self.db_name, symbol=self.symbol, lookback=self.lookback)
        self.lstm_models = [self.ai_core.build_lstm_model() for _ in range(ensemble_size)]
        self.transformer_models = [self.ai_core.build_transformer_model() for _ in range(ensemble_size)]
        self.ppo_model = PPO("MlpPolicy", self.ai_core.env, verbose=0)
        self.performance_metrics = {"win_rate": 0, "profit_factor": 0, "max_drawdown": 0, "sharpe_ratio": 0}

    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    def load_new_data(self, table_name="realtime_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    def update_models_online(self, df):
        try:
            if len(df) < self.lookback * 2:
                logger.warning(f"تعداد کندل‌ها ({len(df)}) برای به‌روزرسانی کافی نیست.")
                return

            df_tech = self.ai_core.technical_analysis(df)
            if df_tech.empty or len(df_tech) < self.lookback:
                logger.warning(f"داده‌های کافی پس از تحلیل تکنیکال وجود ندارد (تعداد کندل‌ها: {len(df_tech)}).")
                return

            X, y = self.ai_core.prepare_data_for_prediction(df_tech)
            if len(X) == 0:
                logger.warning("داده‌های آماده‌شده برای به‌روزرسانی خالی است.")
                return

            for model in self.lstm_models:
                model.fit(X[-32:], y[-32:], epochs=1, batch_size=32, verbose=0)

            X_torch = torch.tensor(X[-32:], dtype=torch.float32)
            y_torch = torch.tensor(y[-32:], dtype=torch.float32).reshape(-1, 1)
            for model in self.transformer_models:
                optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
                loss_fn = nn.MSELoss()
                optimizer.zero_grad()
                pred = model(X_torch)
                loss = loss_fn(pred, y_torch)
                loss.backward()
                optimizer.step()

            self.ppo_model.learn(total_timesteps=1000)
            logger.info("مدل‌ها با موفقیت به‌روز شدند.")
        except Exception as e:
            logger.error(f"خطا در به‌روزرسانی آنلاین مدل‌ها: {e}")

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

            lstm_preds = []
            for model in self.lstm_models:
                pred = model.predict(X[-1].reshape(1, self.lookback, 6), verbose=0)
                lstm_preds.append(np.mean(pred.flatten()))

            X_torch = torch.tensor(X[-1].reshape(1, self.lookback, 6), dtype=torch.float32)
            transformer_preds = []
            for model in self.transformer_models:
                pred = model(X_torch).detach().numpy()
                transformer_preds.append(np.mean(pred.flatten()))

            state = self.ai_core._get_state(df.tail(1))  # استفاده از _get_state با شکل (3,)
            ppo_pred = self.ppo_model.predict(state)[0]

            all_preds = lstm_preds + transformer_preds
            avg_pred = np.mean(all_preds)
            if ppo_pred == 1:
                final_pred = 1 if avg_pred > 0 else 0
            elif ppo_pred == 2:
                final_pred = -1 if avg_pred < 0 else 0
            else:
                final_pred = 1 if avg_pred > 0.5 else -1 if avg_pred < -0.5 else 0

            logger.info(f"سیگنال ترکیبی تولید شد: {final_pred}")
            return final_pred
        except Exception as e:
            logger.error(f"خطا در پیش‌بینی ترکیبی: {e}")
            return 0

    def backtest_and_forward_test(self, historical_df, new_df):
        historical_df_tech = self.ai_core.technical_analysis(historical_df)
        new_df_tech = self.ai_core.technical_analysis(new_df)
        trades = []
        balance = 10000.0
        for i in range(self.lookback, len(historical_df_tech)):
            df_slice = historical_df_tech.iloc[i - self.lookback:i]
            signal = self.ensemble_predict(df_slice)
            next_price = historical_df_tech['close'].iloc[i]
            prev_price = historical_df_tech['close'].iloc[i - 1]
            profit = (next_price - prev_price) * 10 if signal == 1 else (prev_price - next_price) * 10 if signal == -1 else 0
            balance += profit
            trades.append(profit)

        forward_trades = []
        for i in range(self.lookback, len(new_df_tech)):
            df_slice = new_df_tech.iloc[i - self.lookback:i]
            signal = self.ensemble_predict(df_slice)
            next_price = new_df_tech['close'].iloc[i]
            prev_price = new_df_tech['close'].iloc[i - 1]
            profit = (next_price - prev_price) * 10 if signal == 1 else (prev_price - next_price) * 10 if signal == -1 else 0
            forward_trades.append(profit)

        self.calculate_performance_metrics(trades + forward_trades)
        return self.performance_metrics

    def calculate_performance_metrics(self, trades):
        wins = [t for t in trades if t > 0]
        losses = [abs(t) for t in trades if t < 0]
        self.performance_metrics["win_rate"] = len(wins) / len(trades) if trades else 0
        self.performance_metrics["profit_factor"] = sum(wins) / sum(losses) if losses else float('inf')
        balance = 10000
        peak = balance
        max_dd = 0
        for trade in trades:
            balance += trade
            peak = max(peak, balance)
            dd = (peak - balance) / peak
            max_dd = max(max_dd, dd)
        self.performance_metrics["max_drawdown"] = max_dd
        returns = np.array(trades)
        self.performance_metrics["sharpe_ratio"] = returns.mean() / returns.std() if returns.std() != 0 else 0
        logger.info(f"معیارهای عملکرد: {self.performance_metrics}")

    def optimize_models(self):
        if self.performance_metrics["win_rate"] < 0.5 or self.performance_metrics["max_drawdown"] > 0.2:
            logger.warning("عملکرد ضعیف تشخیص داده شد، بهینه‌سازی مدل‌ها...")
            for model in self.lstm_models:
                model.compile(optimizer='adam', loss='mse')
            for model in self.transformer_models:
                for param in model.parameters():
                    param.data = param.data * 0.95
            self.ppo_model = PPO("MlpPolicy", self.ai_core.env, verbose=0)

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
            logger.error(f"خطا در اجرای ماژول یادگیری تطبیقی: {e}")
            return {"win_rate": 0, "max_drawdown": 0, "profit_factor": 0, "sharpe_ratio": 0}

if __name__ == "__main__":
    learning_module = ContinuousLearningModelUpdating(db_name="trading_data.db", symbol="EURUSD_i", lookback=60, ensemble_size=3)
    signal = learning_module.run()
    print(f"سیگنال نهایی: {signal}")