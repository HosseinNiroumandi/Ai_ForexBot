import logging
from datetime import datetime, timedelta
from data_feed import DataFeed
from auto_strategy_generation_optimization import StrategyOptimizer
from continuous_learning_model_updating import ContinuousLearning
from monitoring_system import MonitoringSystem  # فرض می‌کنم این ماژول وجود داره

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """حلقه اصلی ربات تریدینگ"""
    data_feed = DataFeed(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M1)
    monitoring = MonitoringSystem()

    # دریافت داده‌های اولیه
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    historical_data = data_feed.fetch_historical_data(start_date, end_date)
    if historical_data is None:
        logging.error("دریافت داده‌های تاریخی ناموفق بود. ربات متوقف شد.")
        return

    processed_data = data_feed.preprocess_data(historical_data)
    if processed_data is None:
        logging.error("پیش‌پردازش داده‌ها ناموفق بود. ربات متوقف شد.")
        return
    data_feed.save_to_csv(processed_data)

    # بهینه‌سازی استراتژی‌ها
    optimizer = StrategyOptimizer(processed_data)
    top_strategies = optimizer.optimize_strategies(num_strategies=50, top_n=5)
    logging.info(f"استراتژی‌های بهینه‌شده: {top_strategies}")

    # یادگیری مداوم
    learner = ContinuousLearning(processed_data)
    learner.update_models(processed_data)

    # حلقه اصلی برای داده‌های لحظه‌ای
    try:
        while True:
            realtime_data = data_feed.fetch_realtime_data()
            if realtime_data is None:
                logging.warning("داده لحظه‌ای دریافت نشد. ادامه می‌دهیم...")
                continue

            processed_realtime = data_feed.preprocess_data(realtime_data)
            if processed_realtime is None:
                logging.warning("پیش‌پردازش داده لحظه‌ای ناموفق بود. ادامه می‌دهیم...")
                continue
            data_feed.save_to_csv(processed_realtime, filepath="realtime_data.csv")

            # تولید سیگنال
            signal = learner.ensemble_predict(processed_realtime)
            monitoring.log_status({'signal': signal, 'timestamp': datetime.now()})

            # تست استراتژی‌ها روی داده لحظه‌ای (اختیاری)
            for strategy in top_strategies[:1]:  # فقط بهترین استراتژی
                result = optimizer.backtest_strategy(processed_realtime, strategy)
                monitoring.log_status({'strategy_result': result, 'strategy': strategy})

    except KeyboardInterrupt:
        logging.info("ربات توسط کاربر متوقف شد.")
    except Exception as e:
        logging.error(f"خطای غیرمنتظره در حلقه اصلی: {str(e)}")

if __name__ == "__main__":
    main()
