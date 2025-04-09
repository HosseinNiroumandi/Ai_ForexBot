import asyncio
import logging
from datetime import datetime
import sys
import os
import sqlite3
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import MetaTrader5 as mt5
from data_feed import DataFeedModule
from ai_trading_core import AITradingCore
from risk_money_management import RiskMoneyManagement
from order_execution_slippage_control import OrderExecutionSlippageControl
from market_regime_adaptation import MarketRegimeAdaptation
from continuous_learning_model_updating import ContinuousLearningModelUpdating
from security_anti_manipulation import SecurityAntiManipulation
from monitoring_system import MonitoringSystem
from auto_strategy_generation_optimization import AutoStrategyGenerationOptimization

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('trading_bot.log'), logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def initialize_database(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15):
    """ساخت و پر کردن اولیه دیتابیس با داده‌های تاریخی و اقتصادی"""
    data_feed = DataFeedModule(symbol=symbol, timeframe=timeframe)
    try:
        start_date = "2024-10-01"  # 6 ماه قبل
        end_date = datetime.now().strftime("%Y-%m-%d")
        historical_data = data_feed.get_historical_data(start_date, end_date)
        if historical_data is not None:
            data_feed.save_to_database(historical_data, "historical_data")
            logger.info("دیتابیس با داده‌های تاریخی اولیه پر شد.")
        else:
            logger.warning("داده‌های تاریخی دریافت نشدند.")
            return False
        economic_data = data_feed.get_economic_data("UNRATE", start_date, end_date)
        if economic_data is not None:
            data_feed.save_to_database(economic_data, "economic_data")
            logger.info("دیتابیس با داده‌های اقتصادی پر شد.")
        else:
            logger.warning("داده‌های اقتصادی دریافت نشدند.")
            return False
        return True
    except Exception as e:
        logger.error(f"خطا در مقداردهی اولیه دیتابیس: {e}")
        return False

class TradingBot:
    def __init__(self, symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15):
        self.symbol = symbol
        self.timeframe = timeframe
        self.running = True
        self.data_feed = DataFeedModule(symbol=self.symbol, timeframe=self.timeframe)
        self.ai_core = AITradingCore(symbol=self.symbol)
        self.risk_manager = RiskMoneyManagement(symbol=self.symbol)
        self.order_execution = OrderExecutionSlippageControl(symbol=self.symbol)
        self.regime_adaptation = MarketRegimeAdaptation(symbol=self.symbol)
        self.learning_module = ContinuousLearningModelUpdating(symbol=self.symbol)
        self.security_module = SecurityAntiManipulation(symbol=self.symbol)
        self.monitoring_system = MonitoringSystem(symbol=self.symbol)
        self.strategy_module = AutoStrategyGenerationOptimization(symbol=self.symbol)
        self.data_queue = asyncio.Queue()
        self.signal_queue = asyncio.Queue()
        self.trade_params_queue = asyncio.Queue()

    async def data_collection_task(self):
        while self.running:
            try:
                realtime_data = self.data_feed.get_realtime_data()
                if realtime_data is not None:
                    self.data_feed.save_to_database(realtime_data, "realtime_data")
                    conn = sqlite3.connect("trading_data.db")
                    combined_df = pd.read_sql_query(
                        f"SELECT * FROM historical_data WHERE symbol='{self.symbol}' "
                        f"UNION SELECT * FROM realtime_data WHERE symbol='{self.symbol}' "
                        f"ORDER BY time DESC LIMIT 500", conn
                    )
                    conn.close()
                    await self.data_queue.put(combined_df)
                    logger.info(f"داده‌های جدید جمع‌آوری شدند: {len(combined_df)} کندل")
                await asyncio.sleep(60)
            except Exception as e:
                logger.error(f"خطا در جمع‌آوری داده‌ها: {e}")
                await asyncio.sleep(5)

    async def analysis_task(self):
        performance_history = {"ai": 0.5, "strategy": 0.5}
        while self.running:
            try:
                if not self.data_queue.empty():
                    data = await self.data_queue.get()
                    ai_signal = self.ai_core.generate_signal()
                    strategy_signal = self.strategy_module.get_optimized_signal(data)
                    combined_signal = self.generate_combined_signal(data)
                    signal = 1 if combined_signal > 0.5 else -1 if combined_signal < -0.5 else 0
                    if signal != 0:
                        await self.signal_queue.put({"data": data, "signal": signal})
                        logger.info(f"سیگنال ترکیبی: {signal}")
                    performance_history["ai"] = max(0.1, min(0.9, performance_history["ai"] + (ai_signal == signal) * 0.1))
                    performance_history["strategy"] = max(0.1, min(0.9, performance_history["strategy"] + (strategy_signal == signal) * 0.1))
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"خطا در تحلیل: {e}")
                await asyncio.sleep(5)

    def generate_combined_signal(self, df):
        try:
            signal = self.learning_module.ensemble_predict(df)
            logger.info(f"سیگنال ترکیبی تولید شد: {signal}")
            return signal
        except Exception as e:
            logger.error(f"خطا در تولید سیگنال: {e}")
            return 0

    async def regime_adaptation_task(self):
        while self.running:
            try:
                if not self.signal_queue.empty():
                    item = await self.signal_queue.get()
                    trade_params = self.risk_manager.manage_trade(item["signal"])
                    if trade_params:
                        adapted_params = self.regime_adaptation.adapt_strategy(trade_params)
                        if adapted_params:
                            await self.trade_params_queue.put(adapted_params)
                            logger.info("استراتژی با رژیم بازار تطبیق داده شد.")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"خطا در تطبیق رژیم بازار: {e}")
                await asyncio.sleep(5)

    async def execution_task(self):
        while self.running:
            try:
                if not self.trade_params_queue.empty():
                    trade_params = await self.trade_params_queue.get()
                    if self.security_module.secure_trade_execution(trade_params, self.order_execution):
                        logger.info("معامله با موفقیت اجرا شد.")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"خطا در اجرای معامله: {e}")
                await asyncio.sleep(5)

    async def learning_task(self):
        while self.running:
            try:
                metrics = self.learning_module.run()
                if not metrics or "win_rate" not in metrics:
                    logger.warning("معیارهای عملکرد دریافت نشدند یا ناقص هستند.")
                    metrics = {"win_rate": 0, "max_drawdown": 0}
                self.strategy_module.optimize_strategies()
                sleep_time = 300 if (metrics["win_rate"] < 0.6 or metrics["max_drawdown"] > 0.1) else 1800
                logger.info(f"مدل‌ها و استراتژی‌ها به‌روز شدند. معیارها: {metrics}")
                await asyncio.sleep(sleep_time)
            except Exception as e:
                logger.error(f"خطا در بهینه‌سازی: {e}")
                await asyncio.sleep(60)

    async def monitoring_task(self):
        while self.running:
            try:
                self.monitoring_system.run_monitoring(self.learning_module, self.risk_manager)
                logger.info("مانیتورینگ عملکرد تکمیل شد.")
                await asyncio.sleep(3600)
            except Exception as e:
                logger.error(f"خطا در مانیتورینگ: {e}")
                await asyncio.sleep(60)

    async def start(self):
        logger.info("ربات تریدر شروع به کار کرد.")
        tasks = [
            asyncio.create_task(self.data_collection_task()),
            asyncio.create_task(self.analysis_task()),
            asyncio.create_task(self.regime_adaptation_task()),
            asyncio.create_task(self.execution_task()),
            asyncio.create_task(self.learning_task()),
            asyncio.create_task(self.monitoring_task())
        ]
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            self.running = False
            logger.info("ربات متوقف شد.")

if __name__ == "__main__":
    if initialize_database(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15):
        bot = TradingBot(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15)
        asyncio.run(bot.start())
    else:
        logger.error("مقداردهی اولیه دیتابیس ناموفق بود.")