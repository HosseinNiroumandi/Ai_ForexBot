import MetaTrader5 as mt5
import sqlite3
import pandas as pd
import numpy as np
import logging
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='monitoring_log.log', filemode='a')
logger = logging.getLogger(__name__)


class MonitoringSystem:
    def __init__(self, db_name="trading_data.db", symbol="EURUSD_i", min_win_rate=0.6, max_drawdown=0.15,
                 min_profit_factor=1.5):
        """
        مقداردهی اولیه سیستم مانیتورینگ
        :param db_name: نام پایگاه داده
        :param symbol: جفت‌ارز
        :param min_win_rate: حداقل نرخ برد مجاز
        :param max_drawdown: حداکثر افت مجاز
        :param min_profit_factor: حداقل فاکتور سود مجاز
        """
        self.db_name = db_name
        self.symbol = symbol
        self.min_win_rate = min_win_rate
        self.max_drawdown = max_drawdown
        self.min_profit_factor = min_profit_factor

        # اتصال به MetaTrader 5
        if not mt5.initialize():
            raise ConnectionError("Failed to connect to MetaTrader 5")

        # ذخیره تاریخچه معاملات
        self.trade_history = []

    # --- بارگذاری داده‌ها ---
    def load_trade_history(self):
        """
        بارگذاری تاریخچه معاملات از MT5
        """
        trades = mt5.history_deals_get(datetime.now() - timedelta(days=30), datetime.now())
        if trades:
            self.trade_history = [
                {"time": datetime.fromtimestamp(t.deal_time), "profit": t.profit, "volume": t.volume, "type": t.type}
                for t in trades if t.symbol == self.symbol
            ]
        logger.info(f"تعداد معاملات بارگذاری‌شده: {len(self.trade_history)}")

    # --- محاسبه معیارهای عملکرد ---
    def calculate_performance_metrics(self, period="daily"):
        """
        محاسبه معیارهای عملکرد در بازه زمانی مشخص
        :param period: بازه زمانی (daily, weekly, monthly)
        :return: دیکشنری معیارها
        """
        self.load_trade_history()
        if not self.trade_history:
            return None

        df = pd.DataFrame(self.trade_history)
        df['time'] = pd.to_datetime(df['time'])

        # گروه‌بندی بر اساس بازه زمانی
        if period == "daily":
            df_grouped = df.groupby(df['time'].dt.date)
        elif period == "weekly":
            df_grouped = df.groupby(df['time'].dt.isocalendar().week)
        elif period == "monthly":
            df_grouped = df.groupby(df['time'].dt.month)

        metrics = {}
        for name, group in df_grouped:
            wins = group['profit'][group['profit'] > 0].sum()
            losses = abs(group['profit'][group['profit'] < 0].sum())
            total_profit = group['profit'].sum()
            win_count = len(group[group['profit'] > 0])
            trade_count = len(group)

            # محاسبه معیارها
            win_rate = win_count / trade_count if trade_count > 0 else 0
            profit_factor = wins / losses if losses > 0 else float('inf')

            # محاسبه Drawdown
            balance = 10000  # بالانس اولیه فرضی
            peak = balance
            max_dd = 0
            for profit in group['profit']:
                balance += profit
                peak = max(peak, balance)
                dd = (peak - balance) / peak
                max_dd = max(max_dd, dd)

            # محاسبه Sharpe Ratio (ساده‌سازی شده)
            returns = group['profit'].values
            sharpe = returns.mean() / returns.std() if returns.std() != 0 else 0

            metrics[name] = {
                "total_profit": total_profit,
                "win_rate": win_rate,
                "profit_factor": profit_factor,
                "max_drawdown": max_dd,
                "sharpe_ratio": sharpe,
                "trade_count": trade_count
            }

        return metrics

    # --- مانیتورینگ زنده ---
    def live_monitoring(self):
        """
        مانیتورینگ لحظه‌ای وضعیت حساب و معاملات
        :return: دیکشنری وضعیت فعلی
        """
        account_info = mt5.account_info()
        positions = mt5.positions_get(symbol=self.symbol)

        open_trades = len(positions) if positions else 0
        balance = account_info.balance
        equity = account_info.equity
        margin = account_info.margin
        current_drawdown = (balance - equity) / balance if balance > 0 else 0

        status = {
            "timestamp": datetime.now().isoformat(),
            "balance": balance,
            "equity": equity,
            "margin_level": account_info.margin_level,
            "current_drawdown": current_drawdown,
            "open_trades": open_trades
        }
        logger.info(f"وضعیت لحظه‌ای: {status}")
        return status

    # --- تشخیص افت بازدهی ---
    def detect_performance_drop(self, metrics):
        """
        تشخیص افت بازدهی و ارائه هشدار
        :param metrics: معیارهای عملکرد
        :return: True اگر افت تشخیص داده شود، False در غیر این صورت
        """
        latest_metrics = list(metrics.values())[-1] if metrics else {}
        if not latest_metrics:
            return False

        if (latest_metrics["win_rate"] < self.min_win_rate or
                latest_metrics["max_drawdown"] > self.max_drawdown or
                latest_metrics["profit_factor"] < self.min_profit_factor):
            logger.warning(f"افت بازدهی تشخیص داده شد: {latest_metrics}")
            return True
        return False

    # --- ارائه راهکارهای اصلاحی ---
    def suggest_improvements(self, metrics, learning_module, risk_manager):
        """
        ارائه راهکارهای اصلاحی برای بهبود عملکرد
        :param metrics: معیارهای عملکرد
        :param learning_module: نمونه از ContinuousLearningModelUpdating
        :param risk_manager: نمونه از RiskMoneyManagement
        :return: دیکشنری راهکارها
        """
        suggestions = {}

        if self.detect_performance_drop(metrics):
            latest_metrics = list(metrics.values())[-1]

            # کاهش ریسک در صورت Drawdown بالا
            if latest_metrics["max_drawdown"] > self.max_drawdown:
                risk_manager.max_risk_per_trade = max(0.005, risk_manager.max_risk_per_trade * 0.8)  # کاهش 20%
                suggestions["reduce_risk"] = f"ریسک هر معامله به {risk_manager.max_risk_per_trade:.3f} کاهش یافت."

            # به‌روزرسانی مدل‌ها در صورت Win Rate پایین
            if latest_metrics["win_rate"] < self.min_win_rate:
                learning_module.optimize_models()
                suggestions["optimize_models"] = "مدل‌های AI بهینه‌سازی شدند."

            # توقف موقت در صورت Profit Factor پایین
            if latest_metrics["profit_factor"] < self.min_profit_factor:
                suggestions["pause_trading"] = "توصیه به توقف موقت معاملات تا بهبود شرایط."

        logger.info(f"راهکارهای اصلاحی: {suggestions}")
        return suggestions

    # --- تولید گزارش و نمودار ---
    def generate_report(self, metrics, output_dir="reports"):
        """
        تولید گزارش عملکرد و نمودار
        :param metrics: معیارهای عملکرد
        :param output_dir: دایرکتوری ذخیره گزارش
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # گزارش متنی
        report = f"گزارش عملکرد - {datetime.now().isoformat()}\n"
        for period, metric in metrics.items():
            report += f"\nدوره {period}:\n"
            report += f"  سود کل: {metric['total_profit']:.2f}\n"
            report += f"  نرخ برد: {metric['win_rate']:.2%}\n"
            report += f"  فاکتور سود: {metric['profit_factor']:.2f}\n"
            report += f"  حداکثر افت: {metric['max_drawdown']:.2%}\n"
            report += f"  نسبت شارپ: {metric['sharpe_ratio']:.2f}\n"
            report += f"  تعداد معاملات: {metric['trade_count']}\n"

        with open(f"{output_dir}/performance_report.txt", "w") as f:
            f.write(report)

        # نمودار سود و Drawdown
        df = pd.DataFrame(self.trade_history)
        df['cum_profit'] = df['profit'].cumsum()
        df['balance'] = 10000 + df['cum_profit']
        df['peak'] = df['balance'].cummax()
        df['drawdown'] = (df['peak'] - df['balance']) / df['peak']

        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(df['time'], df['cum_profit'], label="Cumulative Profit")
        plt.title("Cumulative Profit Over Time")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(df['time'], df['drawdown'], label="Drawdown", color="red")
        plt.title("Drawdown Over Time")
        plt.legend()

        plt.tight_layout()
        plt.savefig(f"{output_dir}/performance_chart.png")
        plt.close()
        logger.info("گزارش و نمودار عملکرد تولید شد.")

    # --- اجرای کامل مانیتورینگ ---
    def run_monitoring(self, learning_module, risk_manager, period="daily"):
        """
        اجرای کامل سیستم مانیتورینگ
        :param learning_module: نمونه از ContinuousLearningModelUpdating
        :param risk_manager: نمونه از RiskMoneyManagement
        :param period: بازه زمانی تحلیل
        """
        # مانیتورینگ زنده
        live_status = self.live_monitoring()

        # محاسبه معیارها
        metrics = self.calculate_performance_metrics(period)

        # ارائه راهکارها
        suggestions = self.suggest_improvements(metrics, learning_module, risk_manager)

        # تولید گزارش
        if metrics:
            self.generate_report(metrics)

        logger.info(f"مانیتورینگ تکمیل شد. وضعیت: {live_status}, راهکارها: {suggestions}")


if __name__ == "__main__":
    # نمونه اجرا
    from continuous_learning_model_updating import ContinuousLearningModelUpdating
    from risk_money_management import RiskMoneyManagement

    monitoring_system = MonitoringSystem(db_name="trading_data.db", symbol="EURUSD_i",
                                         min_win_rate=0.6, max_drawdown=0.15, min_profit_factor=1.5)
    learning_module = ContinuousLearningModelUpdating(db_name="trading_data.db", symbol="EURUSD_i", lookback=60)
    risk_manager = RiskMoneyManagement(db_name="trading_data.db", symbol="EURUSD_i")

    monitoring_system.run_monitoring(learning_module, risk_manager, period="daily")