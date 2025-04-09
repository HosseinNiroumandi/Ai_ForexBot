import sqlite3
import pandas as pd
import numpy as np
import talib
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import logging
from datetime import datetime
import random
import gym

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='strategy_optimization.log', filemode='a')
logger = logging.getLogger(__name__)


class AutoStrategyGenerationOptimization:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", lookback=60, max_strategies=10):
        self.db_name = db_name
        self.symbol = symbol
        self.lookback = lookback
        self.max_strategies = max_strategies
        self.indicators = {
            "rsi": {"func": talib.RSI, "periods": [14, 21, 28]},
            "ema": {"func": talib.EMA, "periods": [12, 20, 50]},
            "macd": {"func": talib.MACD, "params": [(12, 26, 9)]},
            "bbands": {"func": talib.BBANDS, "periods": [20, 30]}
        }
        self.env = make_vec_env(lambda: self.StrategyEnv(self), n_envs=1)
        self.rl_model = PPO("MlpPolicy", self.env, verbose=0)
        self.strategy_portfolio = []

    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    class StrategyEnv(gym.Env):
        def __init__(self, outer):
            super().__init__()
            self.outer = outer
            self.df = outer.load_data()
            self.step_idx = outer.lookback
            self.position = 0
            obs_size = sum(
                len(config["periods"]) if "periods" in config else 1 for config in self.outer.indicators.values())
            self.action_space = gym.spaces.Discrete(3)
            self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(obs_size,), dtype=np.float32)

        def reset(self):
            self.step_idx = self.outer.lookback
            self.position = 0
            return self._get_state()

        def step(self, action):
            reward = 0
            if action == 1 and self.position != 1:
                self.position = 1
            elif action == 2 and self.position != -1:
                self.position = -1
            elif action == 0:
                self.position = 0
            next_price = self.df['close'].iloc[self.step_idx]
            prev_price = self.df['close'].iloc[self.step_idx - 1]
            if self.position == 1:
                reward = (next_price - prev_price) * 10
            elif self.position == -1:
                reward = (prev_price - next_price) * 10
            self.step_idx += 1
            done = self.step_idx >= len(self.df) - 1
            return self._get_state(), reward, done, {}

        def _get_state(self):
            df_slice = self.df.iloc[self.step_idx - self.outer.lookback:self.step_idx]
            state = []
            for ind_name, ind_config in self.outer.indicators.items():
                if ind_name == "macd":
                    macd, signal, hist = ind_config["func"](df_slice['close'], *ind_config["params"][0])
                    state.append(macd[-1] if not pd.isna(macd[-1]) else 0.0)
                else:
                    for period in ind_config["periods"]:
                        value = ind_config["func"](df_slice['close'], timeperiod=period)
                        state.append(value.iloc[-1] if not pd.isna(value.iloc[-1]) else 0.0)
            return np.array(state)

        def seed(self, seed=None):
            np.random.seed(seed)
            return [seed]

    def generate_random_strategy(self):
        strategy = {"indicators": [], "entry_conditions": [], "exit_conditions": []}
        for ind_name, ind_config in self.indicators.items():
            if random.random() > 0.5:
                if ind_name == "macd":
                    strategy["indicators"].append((ind_name, ind_config["params"][0]))
                else:
                    period = random.choice(ind_config["periods"])
                    strategy["indicators"].append((ind_name, period))
        for ind in strategy["indicators"]:
            if ind[0] == "rsi":
                strategy["entry_conditions"].append((ind[0], "cross_above", random.uniform(30, 50)))
                strategy["exit_conditions"].append((ind[0], "cross_below", random.uniform(50, 70)))
            elif ind[0] == "ema":
                strategy["entry_conditions"].append((ind[0], "price_above", None))
                strategy["exit_conditions"].append((ind[0], "price_below", None))
            elif ind[0] == "macd":
                strategy["entry_conditions"].append((ind[0], "macd_cross_signal", None))
                strategy["exit_conditions"].append((ind[0], "signal_cross_macd", None))
            elif ind[0] == "bbands":
                strategy["entry_conditions"].append((ind[0], "price_below_lower", None))
                strategy["exit_conditions"].append((ind[0], "price_above_upper", None))
        return strategy

    def backtest_strategy(self, strategy, df):
        try:
            balance = 10000.0
            position = 0
            df = df.copy()

            # اضافه کردن اندیکاتورها به دیتافریم
            for ind_name, param in strategy["indicators"]:
                if ind_name == "rsi":
                    df['rsi'] = talib.RSI(df['close'], timeperiod=param)
                elif ind_name == "ema":
                    df[f'ema_{param}'] = talib.EMA(df['close'], timeperiod=param)
                elif ind_name == "macd":
                    df['macd'], df['macd_signal'], _ = talib.MACD(df['close'], *param)
                elif ind_name == "bbands":
                    df['bb_upper'], df['bb_middle'], df['bb_lower'] = talib.BBANDS(df['close'], timeperiod=param)
            df = df.dropna()

            for i in range(1, len(df)):
                entry_triggered = False
                exit_triggered = False

                for ind_name, condition, threshold in strategy["entry_conditions"]:
                    if ind_name == "rsi" and condition == "cross_above":
                        rsi_curr = df['rsi'].iloc[i]
                        rsi_prev = df['rsi'].iloc[i - 1]
                        if rsi_prev < threshold and rsi_curr >= threshold and position == 0:
                            entry_triggered = True
                    elif ind_name == "ema" and condition == "price_above":
                        ema = df[f'ema_{param}'].iloc[i]
                        price = df['close'].iloc[i]
                        if price > ema and position == 0:
                            entry_triggered = True
                    elif ind_name == "macd" and condition == "macd_cross_signal":
                        macd_curr = df['macd'].iloc[i]
                        signal_curr = df['macd_signal'].iloc[i]
                        macd_prev = df['macd'].iloc[i - 1]
                        signal_prev = df['macd_signal'].iloc[i - 1]
                        if macd_prev <= signal_prev and macd_curr > signal_curr and position == 0:
                            entry_triggered = True
                    elif ind_name == "bbands" and condition == "price_below_lower":
                        price = df['close'].iloc[i]
                        lower = df['bb_lower'].iloc[i]
                        if price < lower and position == 0:
                            entry_triggered = True

                for ind_name, condition, threshold in strategy["exit_conditions"]:
                    if ind_name == "rsi" and condition == "cross_below":
                        rsi_curr = df['rsi'].iloc[i]
                        rsi_prev = df['rsi'].iloc[i - 1]
                        if rsi_prev > threshold and rsi_curr <= threshold and position == 1:
                            exit_triggered = True
                    elif ind_name == "ema" and condition == "price_below":
                        ema = df[f'ema_{param}'].iloc[i]
                        price = df['close'].iloc[i]
                        if price < ema and position == 1:
                            exit_triggered = True
                    elif ind_name == "macd" and condition == "signal_cross_macd":
                        macd_curr = df['macd'].iloc[i]
                        signal_curr = df['macd_signal'].iloc[i]
                        macd_prev = df['macd'].iloc[i - 1]
                        signal_prev = df['macd_signal'].iloc[i - 1]
                        if macd_prev >= signal_prev and macd_curr < signal_curr and position == 1:
                            exit_triggered = True
                    elif ind_name == "bbands" and condition == "price_above_upper":
                        price = df['close'].iloc[i]
                        upper = df['bb_upper'].iloc[i]
                        if price > upper and position == 1:
                            exit_triggered = True

                if entry_triggered:
                    position = 1
                    balance -= df['close'].iloc[i]
                elif exit_triggered:
                    position = 0
                    balance += df['close'].iloc[i]

            logger.info(f"نتیجه بکتست استراتژی {strategy}: بالانس {balance}")
            return {"balance": balance}
        except Exception as e:
            logger.error(f"خطا در بکتست استراتژی: {e}")
            return {"balance": -1}

    def evaluate_strategy(self, df, strategy):
        signals = []
        ind_dict = {ind[0]: ind[1] for ind in strategy["indicators"]}

        for ind_name, condition, threshold in strategy["entry_conditions"] + strategy["exit_conditions"]:
            if ind_name == "rsi" and "rsi" in ind_dict:
                rsi = talib.RSI(df['close'], timeperiod=ind_dict["rsi"]).iloc[-1]
                if condition == "cross_above" and rsi > threshold:
                    signals.append(1 if "entry" in condition else 0)
                elif condition == "cross_below" and rsi < threshold:
                    signals.append(-1 if "exit" in condition else 0)
            elif ind_name == "ema" and "ema" in ind_dict:
                ema = talib.EMA(df['close'], timeperiod=ind_dict["ema"]).iloc[-1]
                price = df['close'].iloc[-1]
                if condition == "price_above" and price > ema:
                    signals.append(1)
                elif condition == "price_below" and price < ema:
                    signals.append(-1)
            elif ind_name == "macd" and "macd" in ind_dict:
                macd, signal, _ = talib.MACD(df['close'], *ind_dict["macd"])
                if condition == "macd_cross_signal" and macd[-1] > signal[-1] and macd[-2] <= signal[-2]:
                    signals.append(1)
                elif condition == "signal_cross_macd" and macd[-1] < signal[-1] and macd[-2] >= signal[-2]:
                    signals.append(-1)
            elif ind_name == "bbands" and "bbands" in ind_dict:
                upper, middle, lower = talib.BBANDS(df['close'], timeperiod=ind_dict["bbands"])
                price = df['close'].iloc[-1]
                if condition == "price_below_lower" and price < lower[-1]:
                    signals.append(1)
                elif condition == "price_above_upper" and price > upper[-1]:
                    signals.append(-1)

        if any(s == 1 for s in signals):
            return 1
        elif any(s == -1 for s in signals):
            return -1
        return 0

    def optimize_strategies(self):
        df = self.load_data()
        if df.empty or len(df) < self.lookback * 2:
            logger.warning(f"داده‌های تاریخی کافی نیست (تعداد کندل‌ها: {len(df)})، بهینه‌سازی لغو شد.")
            return

        strategies = [self.generate_random_strategy() for _ in range(200)]
        results = []
        for strategy in strategies:
            try:
                result = self.backtest_strategy(strategy, df.tail(240))
                if result["balance"] > 1000:
                    results.append((strategy, result))
            except Exception as e:
                logger.error(f"خطا در بکتست استراتژی: {e}")

        if not results:
            logger.warning("هیچ استراتژی سوددهی پیدا نشد.")
            default_strategy = {"indicators": [("rsi", 14)], "entry_conditions": [("rsi", "cross_above", 40)],
                                "exit_conditions": [("rsi", "cross_below", 60)]}
            self.strategy_portfolio = [default_strategy]
        else:
            sorted_results = sorted(results, key=lambda x: x[1]["balance"], reverse=True)
            self.strategy_portfolio = [strat for strat, res in sorted_results[:self.max_strategies]]
            try:
                self.rl_model.learn(total_timesteps=10000)
            except Exception as e:
                logger.error(f"خطا در یادگیری PPO: {e}")
        logger.info(f"پورتفوی استراتژی‌ها به‌روز شد: {len(self.strategy_portfolio)} استراتژی انتخاب شد.")

    def get_optimized_signal(self, df):
        if not self.strategy_portfolio:
            logger.warning("پورتفوی استراتژی‌ها خالی است، سیگنال پیش‌فرض 0 برگردانده می‌شود.")
            return 0
        if df.empty or len(df) < self.lookback:
            logger.warning(f"داده‌های کافی برای تولید سیگنال وجود ندارد (تعداد کندل‌ها: {len(df)}).")
            return 0

        signals = [self.evaluate_strategy(df.tail(self.lookback * 2), strategy) for strategy in self.strategy_portfolio]
        if not signals:
            logger.warning("هیچ سیگنالی از استراتژی‌ها تولید نشد، سیگنال پیش‌فرض 0 برگردانده می‌شود.")
            return 0

        return max(set(signals), key=signals.count)

    def run(self):
        self.optimize_strategies()
        df = self.load_data("realtime_data")
        signal = self.get_optimized_signal(df)
        logger.info(f"سیگنال بهینه‌شده: {signal}")
        return signal


if __name__ == "__main__":
    strategy_module = AutoStrategyGenerationOptimization(symbol="EURUSD_i")
    signal = strategy_module.run()
    print(f"سیگنال: {signal}")