import numpy as np
import pandas as pd
import logging
from scipy.optimize import minimize


class StrategyOptimizer:
    def __init__(self, data):
        self.data = data
        self.logger = logging.getLogger(__name__)

    def generate_random_strategy(self):
        """تولید استراتژی تصادفی با اندیکاتورها و شرایط ورود/خروج"""
        indicators = [
            ('rsi', np.random.randint(14, 28)),  # دوره RSI بین 14 تا 28
            ('ema', np.random.randint(12, 50)),  # دوره EMA بین 12 تا 50
            ('macd', (12, 26, 9)),  # MACD با تنظیمات ثابت
            ('bbands', np.random.randint(20, 30))  # دوره Bollinger Bands بین 20 تا 30
        ]
        # انتخاب 1 تا 3 اندیکاتور به صورت تصادفی
        selected_indicators = np.random.choice([0, 1, 2, 3], size=np.random.randint(1, 4), replace=False)
        strategy = {
            'indicators': [indicators[i] for i in selected_indicators],
            'entry_conditions': [],
            'exit_conditions': []
        }
        # اضافه کردن شرایط ورود و خروج برای هر اندیکاتور انتخاب‌شده
        for ind in strategy['indicators']:
            if ind[0] == 'rsi':
                strategy['entry_conditions'].append(('rsi', 'cross_above', np.random.uniform(30, 50)))
                strategy['exit_conditions'].append(('rsi', 'cross_below', np.random.uniform(50, 70)))
            elif ind[0] == 'ema':
                strategy['entry_conditions'].append(('ema', 'price_above', None))
                strategy['exit_conditions'].append(('ema', 'price_below', None))
            elif ind[0] == 'macd':
                strategy['entry_conditions'].append(('macd', 'macd_cross_signal', None))
                strategy['exit_conditions'].append(('macd', 'signal_cross_macd', None))
            elif ind[0] == 'bbands':
                strategy['entry_conditions'].append(('bbands', 'price_below_lower', None))
                strategy['exit_conditions'].append(('bbands', 'price_above_upper', None))
        return strategy

    def calculate_indicators(self, data, indicators):
        """محاسبه اندیکاتورهای تکنیکال برای داده‌ها"""
        df = data.copy()
        for ind in indicators:
            try:
                if ind[0] == 'rsi':
                    df['rsi'] = self._rsi(df['close'], ind[1])
                elif ind[0] == 'ema':
                    df['ema'] = df['close'].ewm(span=ind[1], adjust=False).mean()
                elif ind[0] == 'macd':
                    ema_fast = df['close'].ewm(span=ind[1][0], adjust=False).mean()
                    ema_slow = df['close'].ewm(span=ind[1][1], adjust=False).mean()
                    df['macd'] = ema_fast - ema_slow
                    df['macd_signal'] = df['macd'].ewm(span=ind[1][2], adjust=False).mean()
                elif ind[0] == 'bbands':
                    df['bbands_middle'] = df['close'].rolling(window=ind[1]).mean()
                    df['bbands_std'] = df['close'].rolling(window=ind[1]).std()
                    df['bbands_upper'] = df['bbands_middle'] + 2 * df['bbands_std']
                    df['bbands_lower'] = df['bbands_middle'] - 2 * df['bbands_std']
            except Exception as e:
                self.logger.error(f"خطا در محاسبه اندیکاتور {ind[0]}: {str(e)}")
        return df.dropna()  # حذف ردیف‌هایی که مقادیر NaN دارن

    def _rsi(self, prices, period):
        """محاسبه RSI"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def backtest_strategy(self, data, strategy):
        """بکتست استراتژی با در نظر گرفتن اسپرد"""
        df = self.calculate_indicators(data, strategy['indicators'])
        if len(df) < 60:  # حداقل 60 کندل برای تحلیل
            self.logger.warning(f"تعداد کندل‌ها ({len(df)}) کمتر از 60 است.")
            return {'balance': 10000.0}  # بالانس اولیه بدون تغییر

        balance = 10000.0
        position = 0  # 0: بدون پوزیشن، 1: پوزیشن خرید
        entry_price = 0
        trades = 0

        for i in range(1, len(df)):
            entry_signal = True
            for cond in strategy['entry_conditions']:
                if cond[0] == 'rsi' and 'rsi' in df.columns:
                    if not (df['rsi'].iloc[i - 1] < cond[2] and df['rsi'].iloc[i] > cond[2]):
                        entry_signal = False
                elif cond[0] == 'ema' and 'ema' in df.columns:
                    if not (df['close'].iloc[i] > df['ema'].iloc[i]):
                        entry_signal = False
                elif cond[0] == 'macd' and 'macd' in df.columns:
                    if not (df['macd'].iloc[i - 1] < df['macd_signal'].iloc[i - 1] and df['macd'].iloc[i] >
                            df['macd_signal'].iloc[i]):
                        entry_signal = False
                elif cond[0] == 'bbands' and 'bbands_lower' in df.columns:
                    if not (df['close'].iloc[i] < df['bbands_lower'].iloc[i]):
                        entry_signal = False

            exit_signal = True
            for cond in strategy['exit_conditions']:
                if cond[0] == 'rsi' and 'rsi' in df.columns:
                    if not (df['rsi'].iloc[i - 1] > cond[2] and df['rsi'].iloc[i] < cond[2]):
                        exit_signal = False
                elif cond[0] == 'ema' and 'ema' in df.columns:
                    if not (df['close'].iloc[i] < df['ema'].iloc[i]):
                        exit_signal = False
                elif cond[0] == 'macd' and 'macd' in df.columns:
                    if not (df['macd'].iloc[i - 1] > df['macd_signal'].iloc[i - 1] and df['macd'].iloc[i] <
                            df['macd_signal'].iloc[i]):
                        exit_signal = False
                elif cond[0] == 'bbands' and 'bbands_upper' in df.columns:
                    if not (df['close'].iloc[i] > df['bbands_upper'].iloc[i]):
                        exit_signal = False

            if position == 0 and entry_signal:
                position = 1
                entry_price = df['close'].iloc[i]
                trades += 1
            elif position == 1 and exit_signal:
                profit = (df['close'].iloc[i] - entry_price) * 10000  # فرض لات 0.1
                balance += profit - 0.1  # کسر اسپرد 0.1 پیپ
                position = 0

        return {'balance': balance, 'trades': trades}

    def optimize_strategies(self, num_strategies=50, top_n=10):
        """بهینه‌سازی استراتژی‌ها و انتخاب بهترین‌ها"""
        strategies = [self.generate_random_strategy() for _ in range(num_strategies)]
        results = []
        for strategy in strategies:
            try:
                result = self.backtest_strategy(self.data, strategy)
                results.append((strategy, result['balance'], result['trades']))
            except Exception as e:
                self.logger.error(f"خطا در بکتست استراتژی: {str(e)}")
                results.append((strategy, 10000.0, 0))  # در صورت خطا، بالانس اولیه

        # مرتب‌سازی بر اساس سود و تعداد معاملات (حداقل 5 معامله برای اعتبار)
        results.sort(key=lambda x: (x[1], x[2]), reverse=True)
        top_strategies = [r[0] for r in results if r[2] >= 5][:top_n]  # فقط استراتژی‌هایی با حداقل 5 معامله
        if len(top_strategies) < top_n:
            self.logger.warning(f"تعداد استراتژی‌های معتبر کمتر از {top_n} است: {len(top_strategies)}")
            top_strategies.extend([r[0] for r in results[top_n - len(top_strategies):top_n]])

        self.logger.info(f"{len(top_strategies)} استراتژی سودده انتخاب شد.")
        for strat, bal, tr in results[:top_n]:
            self.logger.info(f"استراتژی: {strat}, بالانس: {bal}, تعداد معاملات: {tr}")
        return top_strategies


if __name__ == "__main__":
    # تست نمونه
    logging.basicConfig(level=logging.INFO)
    data = pd.read_csv("trading_data.csv", index_col='time', parse_dates=True)
    optimizer = StrategyOptimizer(data)
    top_strategies = optimizer.optimize_strategies()
    print("بهترین استراتژی‌ها:", top_strategies)
