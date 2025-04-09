import threading
import queue
import time
import logging
from datetime import datetime
import sys
import os
import sqlite3
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import MetaTrader5 as mt5
import numpy as np
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
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('trading_bot.log'), logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def initialize_database(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15):
    """ساخت و پر کردن اولیه دیتابیس با داده‌های تاریخی و اقتصادی"""
    data_feed = DataFeedModule(symbol=symbol, timeframe=timeframe)
    try:
        start_date = "2024-10-01"  # 6 ماه قبل
        end_date = datetime.now().strftime("%Y-%m-%d")
        # داده‌های تاریخی
        historical_data = data_feed.get_historical_data(start_date, end_date)
        if historical_data is not None:
            data_feed.save_to_database(historical_data, "historical_data")
            logger.info("دیتابیس با داده‌های تاریخی اولیه پر شد.")
        else:
            logger.warning("داده‌های تاریخی دریافت نشدند.")
            return False
        # داده‌های اقتصادی
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
        self.data_queue = queue.Queue()
        self.signal_queue = queue.Queue()
        self.trade_params_queue = queue.Queue()
        self.data_feed = DataFeedModule(symbol=self.symbol, timeframe=self.timeframe)
        self.ai_core = AITradingCore(symbol=self.symbol)
        self.risk_manager = RiskMoneyManagement(symbol=self.symbol)
        self.order_execution = OrderExecutionSlippageControl(symbol=self.symbol)
        self.regime_adaptation = MarketRegimeAdaptation(symbol=self.symbol)
        self.learning_module = ContinuousLearningModelUpdating(symbol=self.symbol)
        self.security_module = SecurityAntiManipulation(symbol=self.symbol)
        self.monitoring_system = MonitoringSystem(symbol=self.symbol)
        self.strategy_module = AutoStrategyGenerationOptimization(symbol=self.symbol)

    def data_collection_task(self):
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
                    logger.info(f"تعداد کندل‌های جمع‌آوری‌شده: {len(combined_df)}")
                    self.data_queue.put(combined_df)
                    logger.info("داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.")
                time.sleep(60)
            except Exception as e:
                logger.error(f"خطا در جمع‌آوری داده‌ها: {e}")
                time.sleep(5)

    def analysis_task(self):
        performance_history = {"ai": 0.5, "strategy": 0.5}
        while self.running:
            try:
                if not self.data_queue.empty():
                    data = self.data_queue.get()
                    if len(data) < self.ai_core.lookback * 2:
                        logger.warning(f"تعداد کندل‌ها ({len(data)}) کمتر از {self.ai_core.lookback * 2} است.")
                        continue
                    ai_signal = self.ai_core.generate_signal()
                    strategy_signal = self.strategy_module.get_optimized_signal(data)
                    if strategy_signal is None:
                        strategy_signal = 0
                    combined_signal = self.generate_combined_signal(data)  # استفاده از تابع جدید
                    signal = 1 if combined_signal > 0.5 else -1 if combined_signal < -0.5 else 0
                    if signal != 0:
                        self.signal_queue.put({"data": data, "signal": signal})
                        logger.info(f"سیگنال ترکیبی نهایی: {signal}")
                    # به‌روزرسانی عملکرد
                    performance_history["ai"] = max(0.1,
                                                    min(0.9, performance_history["ai"] + (ai_signal == signal) * 0.1))
                    performance_history["strategy"] = max(0.1, min(0.9, performance_history["strategy"] + (
                                strategy_signal == signal) * 0.1))
                time.sleep(1)
            except Exception as e:
                logger.error(f"خطا در تحلیل و تولید سیگنال: {e}")
                time.sleep(5)

    def generate_combined_signal(self, df):
        try:
            signal = self.learning_module.ensemble_predict(df)
            logger.info(f"سیگنال ترکیبی تولید شد: {signal}")
            return signal
        except Exception as e:
            logger.error(f"خطا در تولید سیگنال: {e}")
            return 0

    def regime_adaptation_task(self):
        while self.running:
            try:
                if not self.signal_queue.empty():
                    item = self.signal_queue.get()
                    trade_params = self.risk_manager.manage_trade(item["signal"])
                    if trade_params:
                        adapted_params = self.regime_adaptation.adapt_strategy(trade_params)
                        if adapted_params:
                            self.trade_params_queue.put(adapted_params)
                            logger.info("استراتژی با رژیم بازار تطبیق داده شد.")
                time.sleep(1)
            except Exception as e:
                logger.error(f"خطا در تطبیق رژیم بازار: {e}")
                time.sleep(5)

    def execution_task(self):
        while self.running:
            try:
                if not self.trade_params_queue.empty():
                    trade_params = self.trade_params_queue.get()
                    if self.security_module.secure_trade_execution(trade_params, self.order_execution):
                        logger.info("معامله با موفقیت اجرا شد.")
                time.sleep(1)
            except Exception as e:
                logger.error(f"خطا در اجرای معامله: {e}")
                time.sleep(5)

    def learning_task(self):
        while self.running:
            try:
                metrics = self.learning_module.run()
                if not metrics or "win_rate" not in metrics:
                    logger.warning("معیارهای عملکرد دریافت نشدند یا ناقص هستند.")
                    metrics = {"win_rate": 0, "max_drawdown": 0}
                self.strategy_module.optimize_strategies()
                sleep_time = 300 if (metrics["win_rate"] < 0.6 or metrics["max_drawdown"] > 0.1) else 1800
                logger.info(f"مدل‌ها و استراتژی‌ها به‌روز شدند. معیارها: {metrics}")
                time.sleep(sleep_time)
            except Exception as e:
                logger.error(f"خطا در بهینه‌سازی: {e}")
                time.sleep(60)

    def monitoring_task(self):
        while self.running:
            try:
                self.monitoring_system.run_monitoring(self.learning_module, self.risk_manager)
                logger.info("مانیتورینگ عملکرد تکمیل شد.")
                time.sleep(3600)
            except Exception as e:
                logger.error(f"خطا در مانیتورینگ: {e}")
                time.sleep(60)

    def start(self):
        logger.info("ربات تریدر شروع به کار کرد.")
        threads = [
            threading.Thread(target=self.data_collection_task, name="DataCollection"),
            threading.Thread(target=self.analysis_task, name="Analysis"),
            threading.Thread(target=self.regime_adaptation_task, name="RegimeAdaptation"),
            threading.Thread(target=self.execution_task, name="Execution"),
            threading.Thread(target=self.learning_task, name="Learning"),
            threading.Thread(target=self.monitoring_task, name="Monitoring")
        ]
        for thread in threads:
            thread.daemon = True
            thread.start()
        try:
            while self.running:
                time.sleep(10)
        except KeyboardInterrupt:
            self.running = False
            logger.info("ربات متوقف شد.")

if __name__ == "__main__":
    if initialize_database(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15):
        bot = TradingBot(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15)
        bot.start()
    else:
        logger.error("مقداردهی اولیه دیتابیس ناموفق بود. ربات اجرا نمی‌شود.")
