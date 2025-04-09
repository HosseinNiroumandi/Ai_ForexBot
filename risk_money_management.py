import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
import talib
import logging
from datetime import datetime

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class RiskMoneyManagement:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", max_risk_per_trade=0.02, max_drawdown=0.2,
                 leverage=10):
        """
        مقداردهی اولیه ماژول مدیریت سرمایه
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param max_risk_per_trade: حداکثر ریسک در هر معامله (مثلاً 2%)
        :param max_drawdown: حداکثر افت مجاز حساب (مثلاً 20%)
        :param leverage: اهرم حساب
        """
        self.db_name = db_name
        self.symbol = symbol
        self.max_risk_per_trade = max_risk_per_trade
        self.max_drawdown = max_drawdown
        self.leverage = leverage
        account_info = mt5.account_info()
        self.account_balance = account_info.balance if account_info else 10000  # بالانس حساب (پیش‌فرض 10000)
        self.current_drawdown = 0.0

        # همبستگی جفت‌ارزها (داده‌های نمونه)
        self.correlation_matrix = {
            "EURUSD": {"USDJPY": -0.7, "GBPUSD": 0.85},
            "USDJPY": {"EURUSD": -0.7, "GBPUSD": -0.3},
            "GBPUSD": {"EURUSD": 0.85, "USDJPY": -0.3}
        }

    # --- بارگذاری داده‌ها ---
    def load_data(self, table_name="historical_data"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name} WHERE symbol='{self.symbol}'", conn)
        conn.close()
        return df

    # --- محاسبه ATR برای حد ضرر و حد سود داینامیک ---
    def calculate_atr(self, df, period=14):
        """
        محاسبه ATR برای تعیین حد ضرر و حد سود
        :param df: DataFrame داده‌ها
        :param period: دوره ATR
        :return: مقدار ATR
        """
        atr = talib.ATR(df['high'], df['low'], df['close'], timeperiod=period).iloc[-1]
        return atr

    # --- تعیین حجم معامله ---
    def calculate_lot_size(self, stop_loss_pips):
        """
        محاسبه حجم معامله بر اساس ریسک و استاپ‌لاس
        :param stop_loss_pips: استاپ‌لاس به پیپ
        :return: حجم معامله (lot size)
        """
        pip_value = 10  # ارزش هر پیپ برای 1 لات (برای جفت‌ارزهای اصلی)
        risk_amount = self.account_balance * self.max_risk_per_trade
        lot_size = risk_amount / (stop_loss_pips * pip_value * self.leverage)
        lot_size = max(0.01, min(lot_size, 10.0))  # محدود کردن بین 0.01 تا 10 لات
        logger.info(f"حجم معامله محاسبه‌شده: {lot_size:.2f} لات")
        return lot_size

    # --- مدیریت Drawdown ---
    def update_drawdown(self, current_equity):
        self.current_drawdown = (self.account_balance - current_equity) / self.account_balance
        atr = self.calculate_atr(self.load_data())
        risk_factor = min(1.0, max(0.5, 1 - (self.current_drawdown / self.max_drawdown) * (atr / 0.001)))  # تطبیقی
        if self.current_drawdown > self.max_drawdown:
            logger.warning(f"Drawdown بیش از حد: {self.current_drawdown:.2%}, ریسک کاهش یافت: {risk_factor:.2f}")
        return risk_factor

    # --- بررسی همبستگی جفت‌ارزها ---
    def check_correlation(self, other_symbol):
        """
        بررسی همبستگی جفت‌ارزها برای جلوگیری از معاملات هم‌جهت
        :param other_symbol: جفت‌ارز دیگر
        :return: True اگر همبستگی بالا باشد، False در غیر این صورت
        """
        if self.symbol in self.correlation_matrix and other_symbol in self.correlation_matrix[self.symbol]:
            correlation = self.correlation_matrix[self.symbol][other_symbol]
            if abs(correlation) > 0.7:  # آستانه همبستگی
                logger.warning(f"همبستگی بالا بین {self.symbol} و {other_symbol}: {correlation}")
                return True
        return False

    # --- تنظیم حد ضرر و حد سود داینامیک ---
    def set_dynamic_sl_tp(self, df, risk_reward_ratio=2.0):
        """
        تنظیم حد ضرر و حد سود داینامیک
        :param df: DataFrame داده‌ها
        :param risk_reward_ratio: نسبت ریسک به سود (پیش‌فرض 1:2)
        :return: استاپ‌لاس و تیک‌پروفیت به پیپ
        """
        atr = self.calculate_atr(df)
        stop_loss_pips = atr * 2  # استاپ‌لاس 2 برابر ATR
        take_profit_pips = stop_loss_pips * risk_reward_ratio
        return stop_loss_pips, take_profit_pips

    # --- مدیریت ریسک و تولید پارامترهای معامله ---
    def manage_trade(self, signal, other_open_trades=[]):
        if signal == 0:
            return None
        df = self.load_data()
        stop_loss_pips, take_profit_pips = self.set_dynamic_sl_tp(df)
        lot_size = self.calculate_lot_size(stop_loss_pips)
        current_equity = mt5.account_info().equity if mt5.account_info() else self.account_balance
        lot_size *= self.update_drawdown(current_equity)
        current_price = mt5.symbol_info_tick(self.symbol).ask if signal == 1 else mt5.symbol_info_tick(self.symbol).bid
        stop_loss = current_price - (stop_loss_pips * 0.0001) if signal == 1 else current_price + (stop_loss_pips * 0.0001)
        take_profit = current_price + (take_profit_pips * 0.0001) if signal == 1 else current_price - (take_profit_pips * 0.0001)
        return {
            "lot_size": round(lot_size, 2),
            "stop_loss": round(stop_loss, 5),
            "take_profit": round(take_profit, 5),
            "signal": signal
        }

    # --- اجرای معامله با مدیریت ریسک ---
    def execute_managed_trade(self, signal, other_open_trades=[]):
        """
        اجرای معامله با اعمال مدیریت ریسک
        :param signal: سیگنال ترید
        :param other_open_trades: لیست جفت‌ارزهای در حال معامله
        """
        trade_params = self.manage_trade(signal, other_open_trades)
        if not trade_params:
            return

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": trade_params["lot_size"],
            "type": mt5.ORDER_TYPE_BUY if trade_params["signal"] == 1 else mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(self.symbol).ask if trade_params["signal"] == 1 else mt5.symbol_info_tick(
                self.symbol).bid,
            "sl": trade_params["stop_loss"],
            "tp": trade_params["take_profit"],
            "deviation": 20,
            "magic": 123456,
            "comment": "Managed Trade",
            "type_time": mt5.ORDER_TIME_GTC,
        }
        result = mt5.order_send(request)
        if result.retcode == mt5.TRADE_RETCODE_DONE:
            logger.info(f"معامله با موفقیت اجرا شد: {result.order}")
        else:
            logger.error(f"خطا در اجرای معامله: {result.comment}")


if __name__ == "__main__":
    # نمونه اجرا
    if not mt5.initialize():
        raise ConnectionError("Failed to connect to MetaTrader 5")

    risk_manager = RiskMoneyManagement(db_name="trading_data.db", symbol="EURUSD_i", max_risk_per_trade=0.02,
                                       max_drawdown=0.2, leverage=10)
    signal = 1  # نمونه سیگنال خرید
    other_trades = ["GBPUSD"]  # معاملات باز دیگر
    risk_manager.execute_managed_trade(signal, other_trades)