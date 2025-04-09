import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import sqlite3
from sklearn.preprocessing import MinMaxScaler
import logging

# تنظیمات لاگ برای دیباگ و خطایابی
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataFeedModule:
    def __init__(self, symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15, db_name="trading_data.db"):
        """
        مقداردهی اولیه ماژول دیتافید
        :param symbol: جفت‌ارز موردنظر (مثلاً EURUSD)
        :param timeframe: تایم‌فریم (مثلاً M1 برای یک دقیقه)
        :param db_name: نام فایل پایگاه داده SQLite
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.db_name = db_name
        self.FRED_API_KEY = "3e01b56ff0a4e76daa66b4b79e68684f"  # کلید API اقتصادی
        self.scaler = MinMaxScaler()  # ابزار نرمال‌سازی

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            logger.error("اتصال به MetaTrader 5 با مشکل برخورد کرد!")
            raise ConnectionError("Failed to connect to MetaTrader 5")
        logger.info("اتصال به MetaTrader 5 با موفقیت انجام شد.")

    def get_historical_data(self, start_date, end_date):
        """
        دریافت داده‌های تاریخی از MetaTrader 5
        :param start_date: تاریخ شروع (مثلاً '2023-01-01')
        :param end_date: تاریخ پایان (مثلاً '2023-12-31')
        :return: DataFrame شامل داده‌های OHLC
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        rates = mt5.copy_rates_range(self.symbol, self.timeframe, start, end)
        if rates is None or len(rates) == 0:
            logger.warning(f"داده‌ای برای {self.symbol} در بازه زمانی مشخص یافت نشد.")
            return None

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['symbol'] = self.symbol
        df = df[['time', 'open', 'high', 'low', 'close', 'tick_volume', 'symbol']]
        logger.info(f"داده‌های تاریخی برای {self.symbol} با موفقیت دریافت شد.")
        return df

    def get_realtime_data(self):
        """
        دریافت داده‌های لحظه‌ای از MetaTrader 5
        :return: آخرین داده OHLC
        """
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, 1)
        if rates is None or len(rates) == 0:
            logger.warning(f"داده لحظه‌ای برای {self.symbol} دریافت نشد.")
            return None

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['symbol'] = self.symbol
        df = df[['time', 'open', 'high', 'low', 'close', 'tick_volume', 'symbol']]
        logger.info(f"داده لحظه‌ای برای {self.symbol} دریافت شد.")
        return df

    def get_economic_data(self, series_id="UNRATE", start_date="2023-01-01", end_date="2023-12-31"):
        """
        دریافت داده‌های اقتصادی از FRED API
        :param series_id: شناسه سری داده (مثلاً UNRATE برای نرخ بیکاری)
        :param start_date: تاریخ شروع
        :param end_date: تاریخ پایان
        :return: DataFrame شامل داده‌های اقتصادی
        """
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={self.FRED_API_KEY}&file_type=json&observation_start={start_date}&observation_end={end_date}"
        response = requests.get(url)

        if response.status_code != 200:
            logger.error(f"خطا در دریافت داده‌های اقتصادی: {response.status_code}")
            return None

        data = response.json()['observations']
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df = df[['date', 'value']].dropna()
        logger.info(f"داده‌های اقتصادی {series_id} با موفقیت دریافت شد.")
        return df

    def preprocess_data(self, df):
        """
        پیش‌پردازش و نرمال‌سازی داده‌ها
        :param df: DataFrame ورودی
        :return: DataFrame نرمال‌شده
        """
        # حذف مقادیر ناقص
        df = df.dropna()

        # نرمال‌سازی ستون‌های عددی
        numeric_cols = ['open', 'high', 'low', 'close', 'tick_volume'] if 'open' in df.columns else ['value']
        df_normalized = df.copy()
        df_normalized[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])

        logger.info("پیش‌پردازش و نرمال‌سازی داده‌ها با موفقیت انجام شد.")
        return df_normalized

    def save_to_database(self, df, table_name):
        """
        ذخیره داده‌ها در پایگاه داده SQLite
        :param df: DataFrame برای ذخیره
        :param table_name: نام جدول (مثلاً 'historical_data' یا 'economic_data')
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # ساخت جدول اگه وجود نداشت
        if table_name in ['historical_data', 'realtime_data']:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    time TEXT,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    tick_volume REAL,
                    symbol TEXT,
                    PRIMARY KEY (time, symbol)
                )
            """)
        elif table_name == 'economic_data':
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    date TEXT,
                    value REAL,
                    PRIMARY KEY (date)
                )
            """)

        # ذخیره داده‌ها
        try:
            # اگه جدول خالیه، داده‌ها رو اضافه می‌کنیم، وگرنه جایگزین می‌کنیم
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            if cursor.fetchone()[0] == 0:  # جدول خالیه
                df.to_sql(table_name, conn, if_exists='append', index=False)
            else:
                df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.commit()
            logger.info(f"داده‌ها با موفقیت در جدول {table_name} ذخیره شدند.")
        except Exception as e:
            logger.error(f"خطا در ذخیره داده‌ها در جدول {table_name}: {e}")
        finally:
            conn.close()

    def run(self, start_date="2023-01-01", end_date="2023-12-31"):
        """
        اجرای کامل ماژول دیتافید
        """
        # دریافت و ذخیره داده‌های تاریخی
        hist_data = self.get_historical_data(start_date, end_date)
        if hist_data is not None:
            hist_data_processed = self.preprocess_data(hist_data)
            self.save_to_database(hist_data_processed, "historical_data")

        # دریافت و ذخیره داده‌های لحظه‌ای
        realtime_data = self.get_realtime_data()
        if realtime_data is not None:
            realtime_data_processed = self.preprocess_data(realtime_data)
            self.save_to_database(realtime_data_processed, "realtime_data")

        # دریافت و ذخیره داده‌های اقتصادی
        econ_data = self.get_economic_data("UNRATE", start_date, end_date)
        if econ_data is not None:
            econ_data_processed = self.preprocess_data(econ_data)
            self.save_to_database(econ_data_processed, "economic_data")

if __name__ == "__main__":
    # نمونه اجرا
    data_feed = DataFeedModule(symbol="EURUSD_i", timeframe=mt5.TIMEFRAME_M15, db_name="trading_data.db")
    data_feed.run(start_date="2023-01-01", end_date="2023-12-31")
