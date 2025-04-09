import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
import logging
from datetime import datetime, timedelta
import requests
import socket
import time

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='security_log.log', filemode='a')
logger = logging.getLogger(__name__)


class SecurityAntiManipulation:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", max_volatility_spike=5.0, vps_mode=True):
        """
        مقداردهی اولیه ماژول امنیت و ضد کلاهبرداری
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param max_volatility_spike: حداکثر جهش ولتیلیتی مجاز (به درصد)
        :param vps_mode: استفاده از VPS برای امنیت و پایداری
        """
        self.db_name = db_name
        self.symbol = symbol
        self.max_volatility_spike = max_volatility_spike
        self.vps_mode = vps_mode

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")
        logger.info("اتصال به MetaTrader 5 برقرار شد.")

        # تنظیمات امنیتی
        self.connection_timeout = 5  # ثانیه
        self.max_failed_attempts = 3  # حداکثر تلاش ناموفق برای اتصال
        self.last_trade_time = None

    # --- بارگذاری داده‌ها ---
    def load_data(self, table_name="realtime_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}' ORDER BY time DESC LIMIT 100",
                               conn)
        conn.close()
        return df

    # --- بررسی پایداری اتصال ---
    def check_connection_stability(self):
        """
        بررسی پایداری اتصال به بروکر
        :return: True اگر اتصال پایدار باشد، False در غیر این صورت
        """
        failed_attempts = 0
        while failed_attempts < self.max_failed_attempts:
            try:
                socket.setdefaulttimeout(self.connection_timeout)
                tick = mt5.symbol_info_tick(self.symbol)
                if tick is None:
                    raise Exception("عدم دریافت تیک")
                latency = self.measure_latency()
                logger.info(f"اتصال پایدار است. تاخیر: {latency:.2f}ms")
                return True
            except Exception as e:
                failed_attempts += 1
                logger.warning(f"تلاش ناموفق {failed_attempts}/{self.max_failed_attempts}: {e}")
                time.sleep(1)

        logger.error("اتصال به بروکر پایدار نیست!")
        return False

    def measure_latency(self):
        """
        اندازه‌گیری تاخیر اتصال
        :return: تاخیر به میلی‌ثانیه
        """
        start_time = time.time()
        mt5.symbol_info_tick(self.symbol)
        return (time.time() - start_time) * 1000

    # --- تشخیص دستکاری بازار (Spoofing/Manipulation) ---
    def detect_market_manipulation(self, df):
        """
        تشخیص الگوهای دستکاری بازار
        :param df: DataFrame داده‌ها
        :return: True اگر دستکاری تشخیص داده شود، False در غیر این صورت
        """
        # بررسی جهش ناگهانی ولتیلیتی
        atr = df['high'] - df['low']
        atr_spike = atr.pct_change().abs().iloc[-1] * 100
        if atr_spike > self.max_volatility_spike:
            logger.warning(f"جهش ولتیلیتی غیرعادی: {atr_spike:.2f}%")
            return True

        # بررسی حجم غیرعادی
        volume_mean = df['tick_volume'].mean()
        volume_spike = df['tick_volume'].iloc[-1] / volume_mean
        if volume_spike > 5:  # 5 برابر میانگین
            logger.warning(f"حجم غیرعادی: {volume_spike:.2f}x میانگین")
            return True

        # بررسی تغییرات قیمتی ناگهانی
        price_change = df['close'].pct_change().abs().iloc[-1] * 100
        if price_change > 1.0:  # تغییر بیش از 1% در یک کندل
            logger.warning(f"تغییر قیمت ناگهانی: {price_change:.2f}%")
            return True

        return False

    # --- بررسی رفتار مشکوک بروکر ---
    def detect_broker_manipulation(self):
        """
        تشخیص رفتار مشکوک بروکر (مثل تاخیر عمدی یا اسپرد غیرعادی)
        :return: True اگر مشکوک باشد، False در غیر این صورت
        """
        tick = mt5.symbol_info_tick(self.symbol)
        spread = (tick.ask - tick.bid) * 10000  # به پیپ
        if spread > 5.0:  # اسپرد غیرعادی بالا
            logger.warning(f"اسپرد غیرعادی: {spread:.1f} پیپ")
            return True

        # بررسی تاخیر غیرعادی
        latency = self.measure_latency()
        if latency > 200:  # تاخیر بیش از 200ms
            logger.warning(f"تاخیر غیرعادی: {latency:.2f}ms")
            return True

        return False

    # --- بلاک کردن معاملات مشکوک ---
    def block_suspicious_trades(self, trade_params):
        """
        بلاک کردن معاملات در صورت تشخیص رفتار غیرعادی
        :param trade_params: پارامترهای معامله
        :return: True اگر معامله مجاز باشد، False در غیر این صورت
        """
        df = self.load_data()

        if not self.check_connection_stability():
            return False

        if self.detect_market_manipulation(df):
            logger.warning("معامله به دلیل دستکاری بازار بلاک شد.")
            return False

        if self.detect_broker_manipulation():
            logger.warning("معامله به دلیل رفتار مشکوک بروکر بلاک شد.")
            return False

        # بررسی فاصله زمانی معاملات (جلوگیری از اسپم)
        current_time = datetime.now()
        if self.last_trade_time and (current_time - self.last_trade_time).total_seconds() < 5:
            logger.warning("معامله به دلیل فاصله کم زمانی بلاک شد.")
            return False

        self.last_trade_time = current_time
        return True

    # --- اجرای امن معامله ---
    def secure_trade_execution(self, trade_params, order_manager):
        """
        اجرای معامله با اعمال امنیت و ضد کلاهبرداری
        :param trade_params: پارامترهای معامله
        :param order_manager: نمونه از OrderExecutionSlippageControl
        :return: نتیجه اجرا
        """
        if self.block_suspicious_trades(trade_params):
            result = order_manager.smart_execute(trade_params)
            if result:
                logger.info("معامله با موفقیت و به‌صورت امن اجرا شد.")
                self.log_security_status()
                return True
            else:
                logger.error("خطا در اجرای معامله!")
                return False
        else:
            logger.warning("معامله به دلایل امنیتی اجرا نشد.")
            return False

    # --- لاگ‌گیری امنیتی ---
    def log_security_status(self):
        """
        ثبت وضعیت امنیتی برای تحلیل بعدی
        """
        df = self.load_data()
        latency = self.measure_latency()
        tick = mt5.symbol_info_tick(self.symbol)
        spread = (tick.ask - tick.bid) * 10000

        security_status = {
            "timestamp": datetime.now().isoformat(),
            "latency_ms": latency,
            "spread_pips": spread,
            "volatility_spike": (df['high'] - df['low']).pct_change().abs().iloc[-1] * 100,
            "volume_spike": df['tick_volume'].iloc[-1] / df['tick_volume'].mean()
        }
        logger.info(f"وضعیت امنیتی: {security_status}")


if __name__ == "__main__":
    # نمونه اجرا
    from order_execution_slippage_control import OrderExecutionSlippageControl

    security_module = SecurityAntiManipulation(db_name="trading_data.db", symbol="EURUSD_i", max_volatility_spike=5.0,
                                               vps_mode=True)
    order_manager = OrderExecutionSlippageControl(symbol="EURUSD_i", max_spread=2.0, max_slippage_pips=3.0)

    # نمونه پارامترهای معامله
    trade_params = {
        "lot_size": 0.5,
        "stop_loss": 1.0800,
        "take_profit": 1.0900,
        "signal": 1
    }

    result = security_module.secure_trade_execution(trade_params, order_manager)
    if result:
        print("معامله با موفقیت و به‌صورت امن اجرا شد!")
    else:
        print("اجرای معامله ناموفق بود یا به دلایل امنیتی بلاک شد.")
