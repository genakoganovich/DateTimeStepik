from datetime import datetime
from zoneinfo import ZoneInfo

# Шаг 1: Создаем объект tzinfo для Нью-Йорка
ny_tz = ZoneInfo("America/New_York")

# Шаг 2: Передаем его в конструктор datetime
dt_ny = datetime(2025, 7, 15, 12, 0, 0, tzinfo=ny_tz)

print(f"Время в Нью-Йорке: {dt_ny}")
print(f"Объект tzinfo: {dt_ny.tzinfo}")
print(f"Название таймзоны: {dt_ny.tzname()}")
print(f"Смещение от UTC: {dt_ny.utcoffset()}")