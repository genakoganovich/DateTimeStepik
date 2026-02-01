from datetime import datetime
from zoneinfo import ZoneInfo

# Наивный объект, полученный, например, от старой библиотеки
naive_dt = datetime(2025, 9, 25, 18, 30)
print(f"Исходный наивный объект: {naive_dt}")

# Мы знаем, что это московское время
moscow_tz = ZoneInfo("Europe/Moscow")

# Делаем его осведомленным
aware_dt = naive_dt.replace(tzinfo=moscow_tz)
print(f"Стал осведомленным:      {aware_dt}")