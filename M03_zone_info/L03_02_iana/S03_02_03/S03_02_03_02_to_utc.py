from datetime import datetime
from zoneinfo import ZoneInfo

# Пользователь находится в Сиднее
sydney_tz = ZoneInfo("Australia/Sydney")
local_time = datetime(2025, 10, 20, 10, 0, tzinfo=sydney_tz)
print(f"Локальное время пользователя: {local_time}")

# Конвертируем в UTC для сохранения в БД
utc_time_to_store = local_time.astimezone(ZoneInfo("UTC"))
print(f"Время в UTC для хранения:   {utc_time_to_store}")