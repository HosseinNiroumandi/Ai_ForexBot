import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
import talib
import logging
from datetime import datetime, timedelta
import requests

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MarketRegimeAdaptation:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", lookback=60):
        """
        مقداردهی اولیه ماژول مدیریت شرایط خاص
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param lookback: تعداد کندل‌های گذشته برای تحلیل
        """
        self.db_name = db_name
        self.symbol = symbol
        self.lookback = lookback

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")

        # تقویم اخبار اقتصادی (API رایگان)
        self.news_api_key = "f4589bc28bf6470:oqne1vykb49erkg"  # جایگزین با کلید از https://www.tradingeconomics.com/ یا مشابه

    # --- بارگذاری داده‌ها ---
    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    # --- تشخیص رژیم بازار ---
    def detect_market_regime(self, df):
        """
        تشخیص رژیم بازار (روند، رنج، نوسانی)
        :param df: DataFrame داده‌ها
        :return: رژیم بازار (trend, range, volatile)
        """
        # محاسبه ADX برای تشخیص روند
        adx = talib.ADX(df['high'], df['low'], df['close'], timeperiod=14).iloc[-1]

        # محاسبه عرض باند بولینگر برای تشخیص رنج
        upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20)
        bb_width = (upper - lower) / middle
        bb_width_current = bb_width.iloc[-1]

        # محاسبه ATR برای تشخیص نوسانات
        atr = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14).iloc[-1]
        atr_mean = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14).mean()

        if adx > 25:  # روند قوی
            regime = "trend"
        elif bb_width_current < bb_width.mean() * 0.5:  # رنج‌زدگی
            regime = "range"
        elif atr > atr_mean * 1.5:  # نوسانات شدید
            regime = "volatile"
        else:
            regime = "normal"

        logger.info(f"رژیم بازار تشخیص داده‌شده: {regime}")
        return regime

    # --- بررسی زمان‌های نامناسب برای ترید ---
    def check_no_trade_zones(self):
        """
        بررسی زمان‌هایی که نباید ترید کرد
        :return: True اگر ترید مجاز باشد، False در غیر این صورت
        """
        """
           دریافت اخبار اقتصادی مرتبط با جفت‌ارز (مثلاً EUR/USD)
        """
        countries = ["United States", "Euro Area"]  # کشورهای مرتبط با EUR/USD
        current_time = datetime.utcnow()

        # شب‌های جمعه (بعد از 20:00 UTC)
        if current_time.weekday() == 4 and current_time.hour >= 20:
            logger.warning("توقف ترید: شب جمعه")
            return False

        # زمان باز و بسته شدن بازارها (مثلاً 5 دقیقه اول و آخر)
        if current_time.minute < 5 or current_time.minute > 55:
            logger.warning("توقف ترید: زمان باز یا بسته شدن بازار")
            return False

        # اخبار مهم اقتصادی (API نمونه)
        url = f"https://api.tradingeconomics.com/news/country/{country}?importance=high&c={self.news_api_key}&f=json"

        try:
            response = requests.get(url)
            events = response.json()["events"]
            for event in events:
                event_time = datetime.strptime(event["time"], "%Y-%m-%d %H:%M:%S")
                if abs((current_time - event_time).total_seconds()) < 1800:  # 30 دقیقه قبل و بعد
                    logger.warning(f"توقف ترید: خبر مهم در {event['title']}")
                    return False
        except Exception as e:
            logger.error(f"خطا در بررسی تقویم اخبار: {e}")

        return True

    # --- مدیریت معاملات باز ---
    def manage_open_trades(self, trade_params):
        """
        مدیریت معاملات باز و خروج زودهنگام در صورت لزوم
        :param trade_params: پارامترهای معامله (lot_size, stop_loss, take_profit, signal)
        :return: True اگر معامله باید بسته شود، False در غیر این صورت
        """
        df = self.load_data()
        regime = self.detect_market_regime(df)
        current_price = mt5.symbol_info_tick(self.symbol).bid if trade_params["signal"] == 1 else mt5.symbol_info_tick(
            self.symbol).ask

        # اگر بازار برخلاف جهت معامله حرکت کرد
        if trade_params["signal"] == 1 and current_price < trade_params["stop_loss"] * 1.1:  # نزدیک استاپ‌لاس
            logger.warning("خروج زودهنگام: قیمت نزدیک استاپ‌لاس")
            return True
        elif trade_params["signal"] == 2 and current_price > trade_params["stop_loss"] * 0.9:
            logger.warning("خروج زودهنگام: قیمت نزدیک استاپ‌لاس")
            return True

        # اگر رژیم بازار تغییر کرد
        if regime == "volatile" or regime == "range" and trade_params["signal"] in [1, 2]:
            logger.warning(f"خروج زودهنگام: رژیم بازار نامناسب ({regime})")
            return True

        return False

    # --- بستن معامله ---
    def close_trade(self, order_id):
        """
        بستن معامله باز
        :param order_id: شناسه سفارش
        """
        positions = mt5.positions_get(symbol=self.symbol)
        for pos in positions:
            if pos.ticket == order_id:
                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "position": pos.ticket,
                    "symbol": self.symbol,
                    "volume": pos.volume,
                    "type": mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY,
                    "price": mt5.symbol_info_tick(
                        self.symbol).bid if pos.type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(self.symbol).ask,
                    "deviation": 20,
                    "magic": 123456,
                    "comment": "Close Trade",
                    "type_time": mt5.ORDER_TIME_GTC,
                }
                result = mt5.order_send(request)
                if result.retcode == mt5.TRADE_RETCODE_DONE:
                    logger.info(f"معامله {order_id} با موفقیت بسته شد.")
                else:
                    logger.error(f"خطا در بستن معامله: {result.comment}")

    # --- تطبیق استراتژی با رژیم بازار ---
    def adapt_strategy(self, trade_params):
        """
        تطبیق استراتژی با رژیم بازار
        :param trade_params: پارامترهای معامله
        :return: پارامترهای تنظیم‌شده یا None اگر ترید نباید انجام بشه
        """
        if not self.check_no_trade_zones():
            return None

        df = self.load_data()
        regime = self.detect_market_regime(df)

        if regime == "trend":
            # در روند، استاپ‌لاس رو کمی بازتر می‌کنیم
            atr = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14).iloc[-1]
            trade_params["stop_loss"] -= atr * 0.5 if trade_params["signal"] == 1 else -atr * 0.5
            logger.info("استراتژی تطبیق داده‌شده برای بازار روندی")
        elif regime == "range":
            # در رنج، تیک‌پروفیت رو محدودتر می‌کنیم
            trade_params["take_profit"] = trade_params["take_profit"] * 0.8
            logger.info("استراتژی تطبیق داده‌شده برای بازار رنج")
        elif regime == "volatile":
            logger.warning("توقف ترید: بازار بیش از حد نوسانی")
            return None

        return trade_params

    # --- اجرای کامل با تطبیق ---
    def execute_adapted_trade(self, trade_params, order_manager):
        """
        اجرای معامله با تطبیق رژیم بازار
        :param trade_params: پارامترهای معامله از Risk & Money Management
        :param order_manager: نمونه از OrderExecutionSlippageControl
        """
        adapted_params = self.adapt_strategy(trade_params)
        if adapted_params:
            result = order_manager.smart_execute(adapted_params)
            if result:
                # مانیتورینگ معامله باز
                positions = mt5.positions_get(symbol=self.symbol)
                if positions:
                    order_id = positions[-1].ticket
                    if self.manage_open_trades(adapted_params):
                        self.close_trade(order_id)


if __name__ == "__main__":
    # نمونه اجرا
    from order_execution_slippage_control import OrderExecutionSlippageControl

    regime_manager = MarketRegimeAdaptation(db_name="trading_data.db", symbol="EURUSD_i", lookback=60)
    order_manager = OrderExecutionSlippageControl(symbol="EURUSD", max_spread=2.0, max_slippage_pips=3.0)

    # نمونه پارامترهای معامله
    trade_params = {
        "lot_size": 0.5,
        "stop_loss": 1.0800,
        "take_profit": 1.0900,
        "signal": 1
    }

    regime_manager.execute_adapted_trade(trade_params, order_manager)
