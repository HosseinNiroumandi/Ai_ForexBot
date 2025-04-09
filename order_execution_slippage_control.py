import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
import logging
from datetime import datetime

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class OrderExecutionSlippageControl:
    def __init__(self, symbol="EURUSD_i", max_spread=2.0, max_slippage_pips=3.0, vps_mode=True):
        """
        مقداردهی اولیه ماژول مدیریت اوردرها
        :param symbol: جفت‌ارز
        :param max_spread: حداکثر اسپرد مجاز (به پیپ)
        :param max_slippage_pips: حداکثر اسلیپیج مجاز (به پیپ)
        :param vps_mode: استفاده از VPS برای کاهش تاخیر
        """
        self.symbol = symbol
        self.max_spread = max_spread
        self.max_slippage_pips = max_slippage_pips
        self.vps_mode = vps_mode

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")
        logger.info("اتصال به MetaTrader 5 برقرار شد.")

    # --- بررسی اسپرد ---
    def check_spread(self):
        """
        بررسی اسپرد فعلی و تصمیم‌گیری برای اجرا
        :return: True اگر اسپرد مجاز باشد، False در غیر این صورت
        """
        tick = mt5.symbol_info_tick(self.symbol)
        spread = (tick.ask - tick.bid) * 10000  # تبدیل به پیپ
        if spread > self.max_spread:
            logger.warning(f"اسپرد بیش از حد مجاز: {spread:.1f} پیپ")
            return False
        logger.info(f"اسپرد فعلی: {spread:.1f} پیپ")
        return True

    # --- محاسبه تاخیر ---
    def measure_latency(self):
        """
        اندازه‌گیری تاخیر اجرای سفارش
        :return: زمان تاخیر (به میلی‌ثانیه)
        """
        start_time = time.time()
        mt5.symbol_info_tick(self.symbol)  # درخواست نمونه
        latency = (time.time() - start_time) * 1000  # تبدیل به میلی‌ثانیه
        if latency > 100 and self.vps_mode:  # آستانه تاخیر
            logger.warning(f"تاخیر بالا: {latency:.2f} میلی‌ثانیه")
        return latency

    # --- اجرای سفارش با کنترل اسلیپیج ---
    def execute_order(self, trade_params, use_limit_order=False, split_execution=False, split_parts=3):
        """
        اجرای سفارش با کنترل اسلیپیج و مدیریت هوشمند
        :param trade_params: پارامترهای معامله از Risk & Money Management (lot_size, stop_loss, take_profit, signal)
        :param use_limit_order: استفاده از Limit Order به جای Market Order
        :param split_execution: تقسیم حجم به چند بخش
        :param split_parts: تعداد بخش‌های تقسیم
        :return: نتیجه اجرای سفارش
        """
        if not self.check_spread():
            return None

        lot_size = trade_params["lot_size"]
        stop_loss = trade_params["stop_loss"]
        take_profit = trade_params["take_profit"]
        signal = trade_params["signal"]

        # تنظیم نوع سفارش
        tick = mt5.symbol_info_tick(self.symbol)
        current_price = tick.ask if signal == 1 else tick.bid

        # اجرای تقسیم‌شده (در صورت فعال بودن)
        if split_execution:
            split_lot = lot_size / split_parts
            for i in range(split_parts):
                self._send_order(split_lot, stop_loss, take_profit, signal, use_limit_order, current_price)
                time.sleep(0.5)  # فاصله بین سفارش‌ها برای کاهش تاثیر بازار
            logger.info(f"معامله در {split_parts} بخش اجرا شد.")
            return True
        else:
            return self._send_order(lot_size, stop_loss, take_profit, signal, use_limit_order, current_price)

    def _send_order(self, lot_size, stop_loss, take_profit, signal, use_limit_order, current_price):
        """
        ارسال سفارش به MetaTrader
        :return: نتیجه سفارش
        """
        # انتخاب نوع سفارش
        if use_limit_order:
            order_type = mt5.ORDER_TYPE_BUY_LIMIT if signal == 1 else mt5.ORDER_TYPE_SELL_LIMIT
            price = current_price - (self.max_slippage_pips * 0.0001) if signal == 1 else current_price + (
                        self.max_slippage_pips * 0.0001)
        else:
            order_type = mt5.ORDER_TYPE_BUY if signal == 1 else mt5.ORDER_TYPE_SELL
            price = current_price

        request = {
            "action": mt5.TRADE_ACTION_DEAL if not use_limit_order else mt5.TRADE_ACTION_PENDING,
            "symbol": self.symbol,
            "volume": round(lot_size, 2),
            "type": order_type,
            "price": price,
            "sl": stop_loss,
            "tp": take_profit,
            "deviation": int(self.max_slippage_pips * 10),  # انحراف مجاز
            "magic": 123456,
            "comment": "Smart Execution",
            "type_time": mt5.ORDER_TIME_GTC,
        }

        # اندازه‌گیری تاخیر و اجرای سفارش
        latency = self.measure_latency()
        result = mt5.order_send(request)

        if result.retcode == mt5.TRADE_RETCODE_DONE:
            executed_price = result.price
            slippage = abs(executed_price - current_price) * 10000  # اسلیپیج به پیپ
            if slippage > self.max_slippage_pips:
                logger.warning(f"اسلیپیج بالا: {slippage:.1f} پیپ")
            logger.info(f"سفارش با موفقیت اجرا شد: {result.order}, تاخیر: {latency:.2f}ms, اسلیپیج: {slippage:.1f} پیپ")
            return True
        else:
            logger.error(f"خطا در اجرای سفارش: {result.comment}")
            return False

    # --- مانیتورینگ و توقف در شرایط خاص ---
    def monitor_market_conditions(self):
        """
        مانیتورینگ شرایط بازار برای توقف معاملات
        :return: True اگر شرایط مناسب باشد، False در غیر این صورت
        """
        # زمان‌های حساس (مثلاً قبل از اخبار یا آخر هفته)
        current_time = datetime.now()
        if current_time.weekday() == 4 and current_time.hour >= 20:  # جمعه بعد از 20:00 UTC
            logger.warning("معاملات در شب جمعه متوقف شد.")
            return False

        # بررسی اسپرد
        if not self.check_spread():
            return False

        return True

    # --- اجرای هوشمند معامله ---
    def smart_execute(self, trade_params):
        """
        اجرای هوشمند معامله با در نظر گرفتن تمام شرایط
        :param trade_params: پارامترهای معامله
        :return: نتیجه اجرا
        """
        if not self.monitor_market_conditions():
            logger.warning("شرایط بازار برای اجرا مناسب نیست.")
            return None

        # تصمیم‌گیری برای استفاده از Limit Order یا تقسیم حجم
        tick = mt5.symbol_info_tick(self.symbol)
        spread = (tick.ask - tick.bid) * 10000
        use_limit_order = spread > self.max_spread * 0.7  # در اسپرد بالا از Limit Order استفاده کن
        split_execution = trade_params["lot_size"] > 1.0  # برای حجم بالا تقسیم کن

        result = self.execute_order(trade_params, use_limit_order=use_limit_order, split_execution=split_execution)
        return result


if __name__ == "__main__":
    # نمونه اجرا
    order_manager = OrderExecutionSlippageControl(symbol="EURUSD_i", max_spread=2.0, max_slippage_pips=3.0, vps_mode=True)

    # نمونه پارامترهای معامله از Risk & Money Management
    trade_params = {
        "lot_size": 0.5,
        "stop_loss": 1.0800,
        "take_profit": 1.0900,
        "signal": 1  # خرید
    }

    result = order_manager.smart_execute(trade_params)
    if result:
        print("معامله با موفقیت اجرا شد!")
    else:
        print("اجرای معامله ناموفق بود.")