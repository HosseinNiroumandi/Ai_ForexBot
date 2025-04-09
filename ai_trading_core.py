import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
import talib
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification
import requests
from textblob import TextBlob
from stable_baselines3 import PPO, DQN
from stable_baselines3.common.env_util import make_vec_env
import logging
from datetime import datetime
import gym
import shimmy
import inspect

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- یادگیری تقویتی ---
class TradingEnv(gym.Env):
    def __init__(self, core):
        super().__init__()
        self.core = core
        self.df = core.load_data()
        self.position = 0
        self.step_idx = self.core.lookback
        self.action_space = gym.spaces.Discrete(3)  # 0: نگه‌داری، 1: خرید، 2: فروش
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(3,), dtype=np.float32)

    def seed(self, seed=None):
        """تنظیم seed برای تکرارپذیری"""
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.step_idx = self.core.lookback
        self.position = 0
        return self._get_state()

    def step(self, action):
        reward = 0
        if action == 1 and self.position != 1:  # خرید
            self.position = 1
        elif action == 2 and self.position != -1:  # فروش
            self.position = -1
        elif action == 0:
            self.position = 0

        next_price = self.df['close'].iloc[self.step_idx]
        prev_price = self.df['close'].iloc[self.step_idx - 1]
        if self.position == 1:
            reward = (next_price - prev_price) * self.core.leverage
        elif self.position == -1:
            reward = (prev_price - next_price) * self.core.leverage

        self.step_idx += 1
        done = self.step_idx >= len(self.df) - 1
        return self._get_state(), reward, done, {}

    def _get_state(self):
        try:
            if len(self.df) < self.core.lookback:
                logger.warning(f"تعداد کندل‌ها ({len(self.df)}) کافی نیست.")
                return np.zeros(3, dtype=np.float32)
            df_tech = self.core.technical_analysis(self.df.tail(self.core.lookback))
            if df_tech.empty:
                return np.zeros(3, dtype=np.float32)
            state = np.array([
                df_tech['close'].iloc[-1],
                df_tech['rsi'].iloc[-1] if 'rsi' in df_tech else 50.0,
                df_tech['tick_volume'].iloc[-1]
            ], dtype=np.float32)
            return state
        except Exception as e:
            logger.error(f"خطا در محاسبه حالت: {e}")
            return np.zeros(3, dtype=np.float32)

class AITradingCore:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", leverage=10, lookback=60):
        """
        مقداردهی اولیه ماژول
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param leverage: اهرم ترید
        :param lookback: تعداد کندل‌های گذشته
        """
        self.db_name = db_name
        self.symbol = symbol
        self.leverage = leverage
        self.lookback = lookback
        self.scaler = MinMaxScaler()

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")

        # مدل‌های یادگیری عمیق
        self.lstm_model = self.build_lstm_model()
        self.transformer_model = self.build_transformer_model()

        # مدل NLP برای تحلیل اخبار
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.bert_model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

        # محیط یادگیری تقویتی
        self.env = make_vec_env(lambda: TradingEnv(self), n_envs=1)
        self.ppo_model = PPO("MlpPolicy", self.env, verbose=0)
        self.dqn_model = DQN("MlpPolicy", self.env, verbose=0)

    # --- بارگذاری داده‌ها ---
    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    # --- تحلیل تکنیکال ---
    def technical_analysis(self, df):
        try:
            if len(df) < 60:  # کاهش از 200 به 60
                logger.warning(f"تعداد کندل‌ها ({len(df)}) کمتر از 60 است.")
                return pd.DataFrame()
            df = df.copy()
            df['rsi'] = talib.RSI(df['close'], timeperiod=14)
            df['ema_short'] = talib.EMA(df['close'], timeperiod=12)
            df['ema_long'] = talib.EMA(df['close'], timeperiod=50)
            df['macd'], df['macd_signal'], _ = talib.MACD(df['close'])
            df['volume_ema'] = talib.EMA(df['tick_volume'], timeperiod=20)
            df = df.dropna()
            return df
        except Exception as e:
            logger.error(f"خطا در محاسبه اندیکاتورها: {e}")
            return pd.DataFrame()
    # --- تحلیل فاندامنتال ---
    def fundamental_analysis(self):
        conn = sqlite3.connect(self.db_name)
        econ_df = pd.read_sql_query("SELECT * FROM economic_data", conn)
        conn.close()
        econ_score = econ_df['value'].pct_change().mean() * 0.4  # وزن 40%

        api_key = "99dc5b8925594151b5205bfae6837f34"
        url = f"https://newsapi.org/v2/everything?q=forex&apiKey={api_key}"
        response = requests.get(url)
        sentiment = 0
        if response.status_code == 200:
            articles = response.json()['articles'][:10]
            for article in articles:
                inputs = self.tokenizer(article['title'], return_tensors="pt", truncation=True, padding=True)
                outputs = self.bert_model(**inputs)
                sentiment += outputs.logits.softmax(dim=1)[0][1].item()
            sentiment = (sentiment / len(articles)) * 0.6  # وزن 60%
        return econ_score + sentiment

    # --- مدل‌های پیش‌بینی ---
    def build_lstm_model(self):
        model = Sequential()
        model.add(LSTM(100, return_sequences=True, input_shape=(self.lookback, 6)))  # 6 ویژگی
        model.add(Dropout(0.2))
        model.add(LSTM(50))
        model.add(Dense(1, activation='linear'))
        model.compile(optimizer='adam', loss='mse')
        return model

    def build_transformer_model(self):
        class TransformerModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.encoder = nn.TransformerEncoder(
                    nn.TransformerEncoderLayer(d_model=6, nhead=2), num_layers=2
                )
                self.fc = nn.Linear(6, 1)

            def forward(self, x):
                x = self.encoder(x)
                return self.fc(x[:, -1, :])

        return TransformerModel()

    def prepare_data_for_prediction(self, df):
        data = df[['open', 'high', 'low', 'close', 'rsi', 'tick_volume']].values
        data_scaled = self.scaler.fit_transform(data)
        X = np.array([data_scaled[i - self.lookback:i] for i in range(self.lookback, len(data_scaled))])
        y = data_scaled[self.lookback:, 3]  # close
        return X, y

    def train_models(self, df):
        X, y = self.prepare_data_for_prediction(df)
        self.lstm_model.fit(X, y, epochs=20, batch_size=32, verbose=0)  # افزایش epochs و batch_size

        X_torch = torch.tensor(X, dtype=torch.float32)
        y_torch = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
        optimizer = torch.optim.Adam(self.transformer_model.parameters())
        loss_fn = nn.MSELoss()
        for _ in range(20):  # افزایش epochs
            optimizer.zero_grad()
            pred = self.transformer_model(X_torch[:32])
            loss = loss_fn(pred, y_torch[:32])
            loss.backward()
            optimizer.step()

    def predict_trend(self, df):
        try:
            if len(df) < self.lookback:
                logger.warning(f"تعداد کندل‌ها ({len(df)}) برای پیش‌بینی کافی نیست.")
                return 0
            df_tech = self.technical_analysis(df.tail(self.lookback))
            if df_tech.empty:
                return 0
            X, _ = self.prepare_data_for_prediction(df_tech)
            pred = self.lstm_model.predict(X[-1].reshape(1, self.lookback, 6), verbose=0)[0][0]
            return 1 if pred > 0 else -1
        except Exception as e:
            logger.error(f"خطا در پیش‌بینی روند: {e}")
            return 0

    def train_rl_models(self):
        self.ppo_model.learn(total_timesteps=10000)  # افزایش گام‌ها
    # --- بک‌تست ---
    def backtest(self, df):
        balance = 10000
        position = 0
        spread = 0.0002  # اسپرد نمونه برای EURUSD
        for i in range(self.lookback, len(df)):
            df_slice = df.iloc[i - self.lookback:i]
            action = self.ppo_model.predict(self._get_state(df_slice))[0]
            next_price = df['close'].iloc[i]
            prev_price = df['close'].iloc[i - 1]
            if action == 1 and position != 1:
                position = 1
                balance -= spread * self.leverage
            elif action == 2 and position != -1:
                position = -1
                balance -= spread * self.leverage
            elif action == 0:
                position = 0
            if position == 1:
                balance += (next_price - prev_price) * self.leverage
            elif position == -1:
                balance += (prev_price - next_price) * self.leverage
        return balance

    # --- اجرای ترید در MetaTrader ---
    def execute_trade(self, action, lot_size=0.1):
        if action == 1:  # لانگ
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": self.symbol,
                "volume": lot_size,
                "type": mt5.ORDER_TYPE_BUY,
                "price": mt5.symbol_info_tick(self.symbol).ask,
                "deviation": 20,
                "magic": 123456,
                "comment": "AI Trade",
                "type_time": mt5.ORDER_TIME_GTC,
            }
        elif action == 2:  # شورت
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": self.symbol,
                "volume": lot_size,
                "type": mt5.ORDER_TYPE_SELL,
                "price": mt5.symbol_info_tick(self.symbol).bid,
                "deviation": 20,
                "magic": 123456,
                "comment": "AI Trade",
                "type_time": mt5.ORDER_TIME_GTC,
            }
        else:
            return
        mt5.order_send(request)

    # --- تولید سیگنال و اجرا ---
    def generate_signal(self):

        try:
            df = self.load_data()
            logger.info(f"تعداد کندل‌های بارگذاری‌شده: {len(df)}")
            if df.empty or len(df) < self.lookback * 2:
                logger.warning(f"داده‌های کافی برای تولید سیگنال وجود ندارد (تعداد کندل‌ها: {len(df)}).")
                return 0

            df = df.tail(self.lookback * 2)
            logger.info(f"تعداد کندل‌ها پس از برش: {len(df)}")
            df_tech = self.technical_analysis(df)
            if df_tech.empty or len(df_tech) < self.lookback:
                logger.warning(f"داده‌های کافی پس از تحلیل تکنیکال وجود ندارد (تعداد کندل‌ها: {len(df_tech)}).")
                return 0

            fund_score = self.fundamental_analysis()
            self.train_models(df_tech)
            trend = self.predict_trend(df)
            self.train_rl_models()

            # استفاده از محیط RL برای گرفتن state
            env_state = self.env.envs[0]._get_state()  # گرفتن state از TradingEnv
            action = self.ppo_model.predict(env_state)[0]

            combined_score = trend + fund_score + (1 if action == 1 else -1 if action == 2 else 0)
            if combined_score > 0.5:
                signal = 1
            elif combined_score < -0.5:
                signal = 2
            else:
                signal = 0

            self.execute_trade(signal)
            balance = self.backtest(df_tech)
            logger.info(f"سیگنال: {signal}, بک‌تست بالانس: {balance}")
            return signal
        except Exception as e:
            logger.error(f"خطا در تولید سیگنال: {e}")
            return 0

    def _get_state(self, df):
        try:
            if len(df) < 2:
                logger.warning("داده‌های کافی برای محاسبه حالت وجود ندارد.")
                return np.zeros(3)

            latest = df.iloc[-1]
            rsi = latest['rsi'] if 'rsi' in df.columns else 50.0
            volume = latest['tick_volume'] if 'tick_volume' in df.columns else 0.0
            close = latest['close']

            state = np.array([close, rsi, volume], dtype=np.float32)
            return state
        except Exception as e:
            logger.error(f"خطا در تولید حالت: {e}")
            return np.zeros(3)

if __name__ == "__main__":
    ai_core = AITradingCore(db_name="trading_data.db", symbol="EURUSD_i", leverage=10)
    signal = ai_core.generate_signal()
    print(f"سیگنال: {signal}")