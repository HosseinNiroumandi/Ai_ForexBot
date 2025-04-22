"E:\New Bot\pythonProject\Scripts\python.exe" "E:\New Bot\pythonProject\Main.py" 
2025-04-22 11:54:31.454497: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-04-22 11:54:35.496391: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-04-22 11:55:04,742 - INFO - اتصال به MetaTrader 5 با موفقیت انجام شد.
2025-04-22 11:55:04,789 - INFO - داده‌های تاریخی برای EURUSD_i با موفقیت دریافت شد.
2025-04-22 11:55:04,910 - INFO - داده‌ها با موفقیت در جدول historical_data ذخیره شدند.
2025-04-22 11:55:04,910 - INFO - دیتابیس با داده‌های تاریخی اولیه پر شد.
2025-04-22 11:55:05,735 - INFO - داده‌های اقتصادی UNRATE با موفقیت دریافت شد.
2025-04-22 11:55:05,772 - INFO - داده‌ها با موفقیت در جدول economic_data ذخیره شدند.
2025-04-22 11:55:05,772 - INFO - دیتابیس با داده‌های اقتصادی پر شد.
2025-04-22 11:55:05,781 - INFO - اتصال به MetaTrader 5 با موفقیت انجام شد.
2025-04-22 11:55:05.823535: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
E:\New Bot\pythonProject\Lib\site-packages\keras\src\layers\rnn\rnn.py:200: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(**kwargs)
E:\New Bot\pythonProject\Lib\site-packages\torch\nn\modules\transformer.py:385: UserWarning: enable_nested_tensor is True, but self.use_nested_tensor is False because encoder_layer.self_attn.batch_first was not True(use batch_first for better inference performance)
  warnings.warn(
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
E:\New Bot\pythonProject\Lib\site-packages\stable_baselines3\common\vec_env\patch_gym.py:49: UserWarning: You provided an OpenAI Gym environment. We strongly recommend transitioning to Gymnasium environments. Stable-Baselines3 is automatically wrapping your environments in a compatibility layer, which could potentially cause issues.
  warnings.warn(
2025-04-22 11:55:08,560 - INFO - اتصال به MetaTrader 5 برقرار شد.
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
2025-04-22 11:55:10,454 - INFO - اتصال به MetaTrader 5 برقرار شد.
2025-04-22 11:55:10,510 - INFO - ربات تریدر شروع به کار کرد.
2025-04-22 11:55:10,511 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 11:55:10,511 - INFO - وضعیت لحظه‌ای: {'timestamp': '2025-04-22T11:55:10.511474', 'balance': 10000.0, 'equity': 10000.0, 'margin_level': 0.0, 'current_drawdown': 0.0, 'open_trades': 0}
2025-04-22 11:55:10,523 - INFO - تعداد معاملات بارگذاری‌شده: 0
2025-04-22 11:55:10,523 - INFO - راهکارهای اصلاحی: {}
2025-04-22 11:55:10,523 - INFO - مانیتورینگ تکمیل شد. وضعیت: {'timestamp': '2025-04-22T11:55:10.511474', 'balance': 10000.0, 'equity': 10000.0, 'margin_level': 0.0, 'current_drawdown': 0.0, 'open_trades': 0}, راهکارها: {}
2025-04-22 11:55:10,523 - INFO - مانیتورینگ عملکرد تکمیل شد.
2025-04-22 11:55:10,534 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 11:55:10,552 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 11:55:10,552 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 11:55:11,550 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 11:55:11,550 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 11:55:12,290 - INFO - مدل LSTM 1 به‌روز شد.
2025-04-22 11:55:13,999 - INFO - مدل LSTM 2 به‌روز شد.
2025-04-22 11:55:15,914 - INFO - مدل LSTM 3 به‌روز شد.
2025-04-22 11:55:16,149 - INFO - مدل Transformer 1 به‌روز شد.
2025-04-22 11:55:16,261 - INFO - مدل Transformer 2 به‌روز شد.
2025-04-22 11:55:16,355 - INFO - مدل Transformer 3 به‌روز شد.
2025-04-22 11:55:16,370 - ERROR - خطا در اجرای ماژول یادگیری تطبیقی: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:55:16,934 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:16,950 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:16,950 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:16,950 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:16,981 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 41.99869134264709), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 69.01165019534365), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851739999995
2025-04-22 11:55:16,981 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:16,981 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:16,997 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:16,997 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,028 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.863299999995
2025-04-22 11:55:17,043 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 39.4141569564952), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 55.198717337930326), ('bbands', 'price_above_upper', None)]}: بالانس 9998.855430000001
2025-04-22 11:55:17,059 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 38.211131595952324), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 61.34808725647815), ('ema', 'price_below', None)]}: بالانس 10000.004329999989
2025-04-22 11:55:17,059 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 11:55:17,075 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 11:55:17,075 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,090 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 36.24015924977567), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 50.487525315589686), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855589999997
2025-04-22 11:55:17,090 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,122 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:17,122 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,137 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 20)], 'entry_conditions': [('rsi', 'cross_above', 49.61470606967663), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 61.22910086795253), ('ema', 'price_below', None)]}: بالانس 10000.00917999999
2025-04-22 11:55:17,137 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,137 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,153 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 42.040138080650586), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 61.41100373303495), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851499999999
2025-04-22 11:55:17,168 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:17,184 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,200 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 47.311451887175366), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 63.441414157804545), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845179999995
2025-04-22 11:55:17,215 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 44.58151291711111), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 53.90275293857749), ('bbands', 'price_above_upper', None)]}: بالانس 9998.853780000001
2025-04-22 11:55:17,231 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 38.221872731590466)], 'exit_conditions': [('rsi', 'cross_below', 54.1213961468535)]}: بالانس 10000.0
2025-04-22 11:55:17,262 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 30.444800992041564), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 51.98889578693225), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.862989999994
2025-04-22 11:55:17,305 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 37.390142134881984), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.188314881165304), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845809999995
2025-04-22 11:55:17,315 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 11:55:17,316 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:17,318 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,329 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:17,329 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,329 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:17,345 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 41.81037008011792)], 'exit_conditions': [('rsi', 'cross_below', 65.83930643705496)]}: بالانس 9998.8513
2025-04-22 11:55:17,345 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 39.353399421852906)], 'exit_conditions': [('rsi', 'cross_below', 66.16875794149692)]}: بالانس 9998.851120000001
2025-04-22 11:55:17,360 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.010749999996
2025-04-22 11:55:17,376 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:17,376 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 35.72796883486331)], 'exit_conditions': [('rsi', 'cross_below', 69.48485592902173)]}: بالانس 10000.0
2025-04-22 11:55:17,376 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,376 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,407 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 44.84323692685619), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 55.44158917040719), ('ema', 'price_below', None)]}: بالانس 10000.006229999997
2025-04-22 11:55:17,438 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 45.611814259848984), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 61.0867673819573), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.843919999996
2025-04-22 11:55:17,438 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:17,454 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 11:55:17,454 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,470 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,485 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 46.03999653903151), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 63.534720446057584), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:17,516 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:17,516 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,516 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,516 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,526 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 43.79092048107913)], 'exit_conditions': [('rsi', 'cross_below', 54.69716564288807)]}: بالانس 9998.85025
2025-04-22 11:55:17,532 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:17,548 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 33.376946255803425), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 52.49592049280069), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.856049999997
2025-04-22 11:55:17,548 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,564 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 36.3966231862494), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 50.58640315851551), ('bbands', 'price_above_upper', None)]}: بالانس 9998.853880000002
2025-04-22 11:55:17,626 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:17,673 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 31.567458177109874)], 'exit_conditions': [('rsi', 'cross_below', 66.14140129636962)]}: بالانس 10000.0
2025-04-22 11:55:17,689 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 41.51611400974129), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 59.62402273725519), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85801
2025-04-22 11:55:17,689 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,704 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 11:55:17,704 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,736 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 31.092722060394735), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 52.51278708459552), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.863489999992
2025-04-22 11:55:17,751 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 39.33187926416227), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 58.395827600696094), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855259999997
2025-04-22 11:55:17,751 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:17,767 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:17,767 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:17,851 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 42.83920861549291), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 51.976173739710944), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.857499999996
2025-04-22 11:55:17,860 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,887 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 39.12950045894943)], 'exit_conditions': [('rsi', 'cross_below', 55.33064502317754)]}: بالانس 9998.849409999999
2025-04-22 11:55:17,893 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,895 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,913 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 43.3471689361903), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 52.55211675432), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.858029999996
2025-04-22 11:55:17,944 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:17,944 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:17,944 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:17,944 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:17,976 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 41.47513358571924), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 62.971138371286806), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851499999999
2025-04-22 11:55:17,976 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,007 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 44.91167366521698), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 61.44502389105267), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.859969999996
2025-04-22 11:55:18,038 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 32.58459008946836), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 56.12055021677291), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.853009999997
2025-04-22 11:55:18,069 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 36.88836649994795), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 54.7585320046629), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.85778
2025-04-22 11:55:18,069 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:18,085 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 11:55:18,101 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 49.58968131481386), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 58.06985749607824), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.85903
2025-04-22 11:55:18,132 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 40.26294344715577), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 59.199386792850405), ('ema', 'price_below', None)]}: بالانس 10000.006839999996
2025-04-22 11:55:18,132 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 42.80502524912013)], 'exit_conditions': [('rsi', 'cross_below', 51.09307284726941)]}: بالانس 9998.849549999999
2025-04-22 11:55:18,257 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:18,257 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:18,288 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:18,335 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 48.76265966456403), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 68.33690630731378), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85325
2025-04-22 11:55:18,351 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,366 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 36.15038427200549), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 58.5967972618367), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855259999997
2025-04-22 11:55:18,397 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 47.48223111464688), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 69.72479572745178), ('bbands', 'price_above_upper', None)]}: بالانس 9998.84907
2025-04-22 11:55:18,413 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:18,413 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:18,491 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 48.09715379546343), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 63.205840210206944), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.862749999997
2025-04-22 11:55:18,538 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:18,617 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 35.49449148902606), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 56.646524670991084), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.85788
2025-04-22 11:55:18,617 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:18,617 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,679 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 35.45567152818802), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 67.69287739138879), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:18,679 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:18,679 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,679 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:18,695 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:18,710 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,788 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 30.876719910112875), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 68.96474084530573), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.861399999996
2025-04-22 11:55:18,804 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:18,835 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 30.40385702043545), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 64.1783289585925), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.844409999996
2025-04-22 11:55:18,882 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:18,882 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:18,898 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 43.700614439010735), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 63.40090392430888), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.846369999996
2025-04-22 11:55:18,929 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 42.0290914564444), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 63.893320629434555), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845489999996
2025-04-22 11:55:18,929 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:18,945 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:18,976 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:18,976 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,007 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:19,007 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,023 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 48.87872191837948), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 51.75118029152717), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850969999996
2025-04-22 11:55:19,054 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 43.92919737698325), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 52.07916177044956), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.849829999994
2025-04-22 11:55:19,070 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 45.7917783920081), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 56.05268620092984), ('bbands', 'price_above_upper', None)]}: بالانس 9998.853149999999
2025-04-22 11:55:19,070 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,085 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,116 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.014559999996
2025-04-22 11:55:19,116 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,132 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,148 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.010749999996
2025-04-22 11:55:19,148 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,148 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,148 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:19,179 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 38.83031434064472), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 68.78292304799952), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845309999997
2025-04-22 11:55:19,179 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:19,210 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 30.586954828297536), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 51.731461817009084), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855519999997
2025-04-22 11:55:19,226 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 30.79607014651542), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 69.87773330274112), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,241 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 43.01333894060306), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 66.49964079008753), ('ema', 'price_below', None)]}: بالانس 10000.006069999994
2025-04-22 11:55:19,257 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 42.19665485713075), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 61.680161233757325), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845289999996
2025-04-22 11:55:19,288 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:19,320 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 39.70902521247388), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 55.84569252762458), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850809999996
2025-04-22 11:55:19,320 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,335 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:19,351 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20)], 'entry_conditions': [('rsi', 'cross_above', 31.602192567708293), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 59.179642393368184), ('ema', 'price_below', None)]}: بالانس 10000.011459999994
2025-04-22 11:55:19,366 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,382 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 34.045694833503454), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 51.511545157136304), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855519999997
2025-04-22 11:55:19,398 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 11:55:19,398 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,413 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 11:55:19,413 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:19,429 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 38.38057617189308), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 63.30589081762072), ('ema', 'price_below', None)]}: بالانس 10000.010609999998
2025-04-22 11:55:19,445 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 41.327656108143714), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 50.62104082348862), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85142
2025-04-22 11:55:19,476 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 44.66659732622446), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.25592678824091), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 11:55:19,491 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 30.402257028951393), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 59.55982408622509), ('ema', 'price_below', None)]}: بالانس 10000.009489999999
2025-04-22 11:55:19,491 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 11:55:19,507 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,523 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 41.91957398606772), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 57.19905966984782), ('ema', 'price_below', None)]}: بالانس 10000.015619999996
2025-04-22 11:55:19,554 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 46.74561658822232), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 63.96563716701198), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850049999994
2025-04-22 11:55:19,570 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 42.12964334442298), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 56.68085861919068), ('bbands', 'price_above_upper', None)]}: بالانس 9998.855430000001
2025-04-22 11:55:19,586 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 11:55:19,586 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 34.82951277332594)], 'exit_conditions': [('rsi', 'cross_below', 54.874324204934744)]}: بالانس 10000.0
2025-04-22 11:55:19,601 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,601 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,617 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 44.7734326333262), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 68.79020115578848), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.847749999994
2025-04-22 11:55:19,632 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 32.544259237071316)], 'exit_conditions': [('rsi', 'cross_below', 57.173721750303166)]}: بالانس 10000.0
2025-04-22 11:55:19,648 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 42.65355143752756), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 56.27501204203853), ('ema', 'price_below', None)]}: بالانس 10000.009589999994
2025-04-22 11:55:19,664 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 20)], 'entry_conditions': [('rsi', 'cross_above', 45.0068231173063), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 62.19086798965046), ('ema', 'price_below', None)]}: بالانس 10000.006689999993
2025-04-22 11:55:19,679 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 11:55:19,695 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,695 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,711 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 46.33462541832284), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 63.66227003052487), ('ema', 'price_below', None)]}: بالانس 10000.00450999999
2025-04-22 11:55:19,726 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:19,757 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 34.93736674905638), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.2712439331968), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845629999996
2025-04-22 11:55:19,757 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:19,789 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,804 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 33.3743016231311), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 52.29676432878661), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85098
2025-04-22 11:55:19,820 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 41.7005814274068), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 68.39271602965391), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 11:55:19,820 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,836 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 40.478111683585034)], 'exit_conditions': [('rsi', 'cross_below', 57.96198364146588)]}: بالانس 9998.851130000001
2025-04-22 11:55:19,851 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:19,851 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 11:55:19,851 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,851 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:19,867 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 48.00513083398236), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.00560457686798), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85343
2025-04-22 11:55:19,898 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.863299999995
2025-04-22 11:55:19,914 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:19,914 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,914 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,929 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 38.23677566364088), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 59.30790417663306), ('ema', 'price_below', None)]}: بالانس 10000.009959999998
2025-04-22 11:55:19,929 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 11:55:19,945 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 33.907957274583694), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 59.497968370113725), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.844359999996
2025-04-22 11:55:19,976 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:19,976 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:19,992 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 11:55:20,054 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 11:55:20,070 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 11:55:20,086 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.863299999995
2025-04-22 11:55:20,101 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 11:55:20,101 - ERROR - خطا در یادگیری PPO: -1
2025-04-22 11:55:20,101 - INFO - پورتفوی استراتژی‌ها به‌روز شد: 10 استراتژی انتخاب شد.
2025-04-22 11:55:20,101 - INFO - مدل‌ها و استراتژی‌ها به‌روز شدند. معیارها: {'win_rate': 0, 'max_drawdown': 0, 'profit_factor': 0, 'sharpe_ratio': 0}
2025-04-22 11:55:24,409 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:55:24,411 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 11:56:10,553 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 11:56:10,580 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 11:56:10,642 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 11:56:10,642 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 11:56:11,518 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 11:56:11,518 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 11:56:15,159 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:56:15,159 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 11:57:10,652 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 11:57:10,661 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 11:57:10,723 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 11:57:10,723 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 11:57:11,208 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 11:57:11,208 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 11:57:14,856 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:57:14,856 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 11:58:10,728 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 11:58:10,738 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 11:58:10,763 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 11:58:10,768 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 11:58:10,938 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 11:58:10,938 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 11:58:14,213 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:58:14,213 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 11:59:10,768 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 11:59:10,774 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 11:59:10,806 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 11:59:10,806 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 11:59:11,306 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 11:59:11,306 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 11:59:14,525 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 11:59:14,541 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 12:00:10,818 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 12:00:10,831 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 12:00:10,847 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 12:00:10,847 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 12:00:11,598 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 12:00:11,598 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 12:00:15,037 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 12:00:15,037 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 12:00:20,243 - INFO - مدل LSTM 1 به‌روز شد.
2025-04-22 12:00:20,321 - INFO - مدل LSTM 2 به‌روز شد.
2025-04-22 12:00:20,430 - INFO - مدل LSTM 3 به‌روز شد.
2025-04-22 12:00:20,477 - INFO - مدل Transformer 1 به‌روز شد.
2025-04-22 12:00:20,509 - INFO - مدل Transformer 2 به‌روز شد.
2025-04-22 12:00:20,540 - INFO - مدل Transformer 3 به‌روز شد.
2025-04-22 12:00:20,540 - ERROR - خطا در اجرای ماژول یادگیری تطبیقی: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 12:00:20,571 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,571 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,587 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,603 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:20,618 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 30.044636518560555), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 56.367783819059824), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.014169999995
2025-04-22 12:00:20,618 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,634 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 31.729951481073368), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 59.107865006122026), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:20,634 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,634 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 12:00:20,634 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:20,650 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:20,650 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:20,650 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,665 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,681 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 45.86435904037314), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.60769666635231), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.011249999998
2025-04-22 12:00:20,681 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,681 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,681 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:20,681 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,696 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 49.3128360827513)], 'exit_conditions': [('rsi', 'cross_below', 68.45666940928318)]}: بالانس 9998.852210000001
2025-04-22 12:00:20,696 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,712 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 31.240298015218755), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 51.973737214545125), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85098
2025-04-22 12:00:20,729 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:20,729 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,744 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20)], 'entry_conditions': [('rsi', 'cross_above', 36.60307787112605), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 58.1128857809311), ('ema', 'price_below', None)]}: بالانس 10000.011009999993
2025-04-22 12:00:20,744 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,744 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,744 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,759 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 32.706932216822636), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 54.97332977821864), ('ema', 'price_below', None)]}: بالانس 10000.015150000001
2025-04-22 12:00:20,791 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 45.213674626102765), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.6612655459341), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.859909999996
2025-04-22 12:00:20,791 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,791 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,806 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,806 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,822 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 31.598643596252927), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.51720108689648), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.844039999996
2025-04-22 12:00:20,822 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:20,837 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 33.88754319119425)], 'exit_conditions': [('rsi', 'cross_below', 57.183093685177504)]}: بالانس 10000.0
2025-04-22 12:00:20,837 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:20,837 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:20,853 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:20,853 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:20,853 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,869 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:20,884 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:20,884 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,900 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:20,900 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,916 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:20,951 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 37.10710404882909), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 69.65923531780129), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.846929999994
2025-04-22 12:00:20,957 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:20,957 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:20,967 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:20,981 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 42.398664752680354), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 67.99033052793723), ('ema', 'price_below', None)]}: بالانس 9998.853749999995
2025-04-22 12:00:21,000 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 33.287530007041596), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 50.47016430781618), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850799999997
2025-04-22 12:00:21,016 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 38.7608857742912), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 63.51312177693511), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.011749999996
2025-04-22 12:00:21,016 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,031 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.014559999996
2025-04-22 12:00:21,049 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.010749999996
2025-04-22 12:00:21,071 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 46.58710598130446), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 51.41101005456685), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.857109999995
2025-04-22 12:00:21,071 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,076 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,079 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.010749999996
2025-04-22 12:00:21,086 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,086 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,086 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,106 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 48.95076313541755), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 67.6091883508908), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.846759999999
2025-04-22 12:00:21,116 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,136 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 32.67579622684972), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 59.119081496657664), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855629999996
2025-04-22 12:00:21,136 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,141 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,158 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:21,174 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 48.15717332400623), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 61.666582317857575), ('bbands', 'price_above_upper', None)]}: بالانس 9998.84979
2025-04-22 12:00:21,190 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 48.16452850786752), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.8802127409128), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845179999995
2025-04-22 12:00:21,196 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:21,196 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,221 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 38.75794680017645), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.32999370245527), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845809999995
2025-04-22 12:00:21,222 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:21,222 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,238 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 32.86291786078499), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 64.574220264317), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.844899999996
2025-04-22 12:00:21,254 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,256 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,256 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:21,275 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 49.36263834938175), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 66.72585089847504), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845419999998
2025-04-22 12:00:21,285 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,295 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:21,295 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 34.50295381782642)], 'exit_conditions': [('rsi', 'cross_below', 68.80538289227685)]}: بالانس 10000.0
2025-04-22 12:00:21,315 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,325 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 47.63568382622267), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.05517591193859), ('bbands', 'price_above_upper', None)]}: بالانس 9998.84907
2025-04-22 12:00:21,338 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 33.758529114937936), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 60.67715044137785), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851499999999
2025-04-22 12:00:21,346 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:21,361 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:21,371 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:21,374 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,381 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 31.633075087659982)], 'exit_conditions': [('rsi', 'cross_below', 65.67963698306453)]}: بالانس 10000.0
2025-04-22 12:00:21,394 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,411 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 49.321255307764446), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 62.149532357536856), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.845079999996
2025-04-22 12:00:21,426 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 39.69803817145059), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 51.05026647491878), ('ema', 'price_below', None)]}: بالانس 10000.012659999995
2025-04-22 12:00:21,435 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:21,437 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,439 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,440 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,442 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,467 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 35.2780595027696), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 62.675094182933606), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.860259999992
2025-04-22 12:00:21,467 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:21,494 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 12:00:21,516 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 47.676151629058296), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 58.99793962653846), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851749999994
2025-04-22 12:00:21,533 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,541 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 43.854721498049386)], 'exit_conditions': [('rsi', 'cross_below', 53.1680825860707)]}: بالانس 9998.851539999998
2025-04-22 12:00:21,555 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9))], 'entry_conditions': [('macd', 'macd_cross_signal', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None)]}: بالانس 9998.855339999996
2025-04-22 12:00:21,567 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 35.92164726140875), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 69.14937898309228), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.846569999996
2025-04-22 12:00:21,575 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,590 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 39.03656454881033), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 67.98513561256149), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:21,597 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:21,600 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,612 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 36.90687453008064), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 50.444518474121466), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85197
2025-04-22 12:00:21,621 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:21,636 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 30.229028007227882), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 58.090539609032646), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.017100000001
2025-04-22 12:00:21,646 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 44.61030401202981), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 58.323217600870805), ('ema', 'price_below', None)]}: بالانس 10000.00662999999
2025-04-22 12:00:21,661 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 36.756834165532055), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 68.03158456244532), ('ema', 'price_below', None)]}: بالانس 10000.00915
2025-04-22 12:00:21,666 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,667 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,676 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:21,676 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,687 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 40.70096851261432), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 52.908689680294074), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.857499999996
2025-04-22 12:00:21,706 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 46.34879939982798), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 50.1669836473542), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85023
2025-04-22 12:00:21,731 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 30.12391684462718), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 64.4378046345485), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:21,737 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 45.4777420582453)], 'exit_conditions': [('rsi', 'cross_below', 62.10088795750635)]}: بالانس 9998.851120000001
2025-04-22 12:00:21,737 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,758 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 39.90959572648947), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 50.469671932241965), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.855159999997
2025-04-22 12:00:21,758 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,767 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:21,767 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:21,767 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,781 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 44.53622703946468), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 62.5610158581906), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:21,786 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,786 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,796 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:21,796 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,796 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21)], 'entry_conditions': [('rsi', 'cross_above', 41.41485753285984)], 'exit_conditions': [('rsi', 'cross_below', 58.530129644402905)]}: بالانس 9998.85025
2025-04-22 12:00:21,805 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,810 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 32.61629406475298)], 'exit_conditions': [('rsi', 'cross_below', 55.14563473936747)]}: بالانس 10000.0
2025-04-22 12:00:21,816 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 45.50175138274511)], 'exit_conditions': [('rsi', 'cross_below', 67.45021797309805)]}: بالانس 9998.8547
2025-04-22 12:00:21,836 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 46.742156337374865), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 66.27498366287432), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.012269999996
2025-04-22 12:00:21,836 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:21,846 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 38.37437220190773), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 54.197225832060724), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851499999999
2025-04-22 12:00:21,856 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:21,856 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,856 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,856 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,856 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,867 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:21,867 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:21,876 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 48.862099525847825)], 'exit_conditions': [('rsi', 'cross_below', 59.29863891286004)]}: بالانس 9998.849950000002
2025-04-22 12:00:21,876 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 50)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.01069
2025-04-22 12:00:21,876 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:21,906 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 30.464586887500232), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 59.50621603279157), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.854759999998
2025-04-22 12:00:21,911 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:21,926 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:21,936 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 44.725406724759395), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 57.34128561129214), ('ema', 'price_below', None)]}: بالانس 10000.015619999996
2025-04-22 12:00:21,956 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 12:00:21,976 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 42.16664670691866), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 67.64675216411378), ('bbands', 'price_above_upper', None)]}: بالانس 9998.851499999999
2025-04-22 12:00:21,990 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:22,016 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 20), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 47.10537316461249), ('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 65.77239682516337), ('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.011169999998
2025-04-22 12:00:22,026 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:22,036 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:22,036 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:22,045 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 20), ('bbands', 20)], 'entry_conditions': [('ema', 'price_above', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('ema', 'price_below', None), ('bbands', 'price_above_upper', None)]}: بالانس 10000.014559999996
2025-04-22 12:00:22,056 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:22,056 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,067 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 46.96862318498911), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 55.31706134966509), ('ema', 'price_below', None)]}: بالانس 10000.01109
2025-04-22 12:00:22,067 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:22,086 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 47.698652315187886), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 61.11913256259497), ('ema', 'price_below', None)]}: بالانس 10000.009419999995
2025-04-22 12:00:22,108 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 49.33213995414123), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 53.611695289887436), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.855949999997
2025-04-22 12:00:22,108 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,116 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 34.394064957905215)], 'exit_conditions': [('rsi', 'cross_below', 66.01261758738724)]}: بالانس 10000.0
2025-04-22 12:00:22,116 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:22,126 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:22,126 - INFO - نتیجه بکتست استراتژی {'indicators': [], 'entry_conditions': [], 'exit_conditions': []}: بالانس 10000.0
2025-04-22 12:00:22,146 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 44.02496566587492), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 62.228767358246984), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.850549999996
2025-04-22 12:00:22,156 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28), ('ema', 50)], 'entry_conditions': [('rsi', 'cross_above', 33.63219141456905), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 67.04161447561236), ('ema', 'price_below', None)]}: بالانس 10000.00892
2025-04-22 12:00:22,191 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('ema', 20), ('macd', (12, 26, 9)), ('bbands', 20)], 'entry_conditions': [('rsi', 'cross_above', 31.338339772458216), ('ema', 'price_above', None), ('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 69.41730080409172), ('ema', 'price_below', None), ('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.858859999997
2025-04-22 12:00:22,198 - INFO - نتیجه بکتست استراتژی {'indicators': [('ema', 12)], 'entry_conditions': [('ema', 'price_above', None)], 'exit_conditions': [('ema', 'price_below', None)]}: بالانس 10000.005699999992
2025-04-22 12:00:22,214 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('bbands', 30)], 'entry_conditions': [('rsi', 'cross_above', 42.669092418825585), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('rsi', 'cross_below', 58.25394062572156), ('bbands', 'price_above_upper', None)]}: بالانس 9998.85591
2025-04-22 12:00:22,230 - INFO - نتیجه بکتست استراتژی {'indicators': [('macd', (12, 26, 9)), ('bbands', 30)], 'entry_conditions': [('macd', 'macd_cross_signal', None), ('bbands', 'price_below_lower', None)], 'exit_conditions': [('macd', 'signal_cross_macd', None), ('bbands', 'price_above_upper', None)]}: بالانس 9998.852289999995
2025-04-22 12:00:22,236 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:22,246 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:22,246 - ERROR - خطا در بکتست استراتژی: 'ema_30'
2025-04-22 12:00:22,246 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,262 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 21), ('ema', 12)], 'entry_conditions': [('rsi', 'cross_above', 36.44694693647904), ('ema', 'price_above', None)], 'exit_conditions': [('rsi', 'cross_below', 59.19404777566134), ('ema', 'price_below', None)]}: بالانس 10000.00695999999
2025-04-22 12:00:22,267 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 30)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85432
2025-04-22 12:00:22,267 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,278 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 28)], 'entry_conditions': [('rsi', 'cross_above', 33.59153805930076)], 'exit_conditions': [('rsi', 'cross_below', 66.28849101955448)]}: بالانس 10000.0
2025-04-22 12:00:22,278 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,285 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:22,291 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:22,310 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14), ('macd', (12, 26, 9))], 'entry_conditions': [('rsi', 'cross_above', 30.286863770905196), ('macd', 'macd_cross_signal', None)], 'exit_conditions': [('rsi', 'cross_below', 60.72301001775078), ('macd', 'signal_cross_macd', None)]}: بالانس 9998.844529999997
2025-04-22 12:00:22,316 - INFO - نتیجه بکتست استراتژی {'indicators': [('bbands', 20)], 'entry_conditions': [('bbands', 'price_below_lower', None)], 'exit_conditions': [('bbands', 'price_above_upper', None)]}: بالانس 9998.85528
2025-04-22 12:00:22,316 - ERROR - خطا در بکتست استراتژی: 'ema_20'
2025-04-22 12:00:22,326 - INFO - نتیجه بکتست استراتژی {'indicators': [('rsi', 14)], 'entry_conditions': [('rsi', 'cross_above', 48.12578813939109)], 'exit_conditions': [('rsi', 'cross_below', 68.76236426309185)]}: بالانس 9998.8487
2025-04-22 12:00:22,326 - ERROR - خطا در بکتست استراتژی: 'ema_(12, 26, 9)'
2025-04-22 12:00:22,326 - ERROR - خطا در یادگیری PPO: -1
2025-04-22 12:00:22,326 - INFO - پورتفوی استراتژی‌ها به‌روز شد: 10 استراتژی انتخاب شد.
2025-04-22 12:00:22,326 - INFO - مدل‌ها و استراتژی‌ها به‌روز شدند. معیارها: {'win_rate': 0, 'max_drawdown': 0, 'profit_factor': 0, 'sharpe_ratio': 0}
2025-04-22 12:01:10,855 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 12:01:10,867 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 12:01:10,900 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 12:01:10,900 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 12:01:11,158 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 12:01:11,158 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 12:01:14,864 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 12:01:14,864 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 12:02:10,913 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 12:02:10,941 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 12:02:10,972 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 12:02:10,972 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 12:02:11,926 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 12:02:11,926 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 12:02:15,218 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 12:02:15,218 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 12:03:10,975 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 12:03:10,979 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 12:03:11,010 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 12:03:11,010 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 12:03:11,323 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 12:03:11,323 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 12:03:14,651 - ERROR - خطا در تولید سیگنال: could not broadcast input array from shape (60,6) into shape (3,)
2025-04-22 12:03:14,651 - ERROR - خطا در تحلیل و تولید سیگنال: -1
2025-04-22 12:04:11,013 - INFO - داده لحظه‌ای برای EURUSD_i دریافت شد.
2025-04-22 12:04:11,027 - INFO - داده‌ها با موفقیت در جدول realtime_data ذخیره شدند.
2025-04-22 12:04:11,049 - INFO - تعداد کندل‌های جمع‌آوری‌شده: 500
2025-04-22 12:04:11,049 - INFO - داده‌های جدید جمع‌آوری و با داده‌های تاریخی ترکیب شدند.
2025-04-22 12:04:11,720 - INFO - تعداد کندل‌های بارگذاری‌شده: 13532
2025-04-22 12:04:11,720 - INFO - تعداد کندل‌ها پس از برش: 120
2025-04-22 12:04:12,140 - INFO - ربات متوقف شد.

Process finished with exit code 0
