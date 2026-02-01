from datetime import datetime, timezone, timedelta

# Попытка представить Берлинское время зимой
berlin_winter_tz = timezone(timedelta(hours=1))
winter_time = datetime(2025, 1, 15, 12, 0, tzinfo=berlin_winter_tz)
print(f"Время зимой: {winter_time}") # Корректно для этой даты

# Попытка использовать то же смещение для летней даты
summer_time = datetime(2025, 7, 15, 12, 0, tzinfo=berlin_winter_tz)
print(f"Время летом: {summer_time}") # НЕКОРРЕКТНО! Летом смещение должно быть +02:00