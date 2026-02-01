from datetime import datetime, timezone, timedelta

# Создадим tzinfo для смещения +05:30 (время в Индии)
india_offset = timedelta(hours=5, minutes=30)
india_tz = timezone(india_offset)

# Создадим осведомленный объект с этим смещением
india_time = datetime(2025, 9, 25, 17, 30, 0, tzinfo=india_tz)

print(f"Время в Индии: {india_time}")
print(f"Объект tzinfo: {india_time.tzinfo}")
print(f"Смещение от UTC: {india_time.utcoffset()}")