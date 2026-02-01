from datetime import datetime
from zoneinfo import ZoneInfo

# Создаем объект tzinfo для Берлина
berlin_tz = ZoneInfo("Europe/Berlin")

# 1. Дата зимой (стандартное время, CET)
dt_winter = datetime(2025, 1, 15, 12, 0, 0, tzinfo=berlin_tz)
print(f"Зима в Берлине:")
print(f"  Время: {dt_winter}")
print(f"  Смещение: {dt_winter.utcoffset()} ({dt_winter.tzname()})")

print("-" * 20)

# 2. Дата летом (летнее время, CEST)
dt_summer = datetime(2025, 7, 15, 12, 0, 0, tzinfo=berlin_tz)
print(f"Лето в Берлине:")
print(f"  Время: {dt_summer}")
print(f"  Смещение: {dt_summer.utcoffset()} ({dt_summer.tzname()})")