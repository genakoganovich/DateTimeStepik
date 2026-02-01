from datetime import datetime
from zoneinfo import ZoneInfo

# Время, извлеченное из БД (уже в UTC)
utc_time_from_db = datetime(2025, 10, 19, 23, 0, tzinfo=ZoneInfo("UTC"))

# Конвертируем в часовой пояс пользователя из Берлина
berlin_tz = ZoneInfo("Europe/Berlin")
local_time_to_display = utc_time_from_db.astimezone(berlin_tz)

print(f"Время из БД (UTC):        {utc_time_from_db}")
print(f"Время для пользователя:   {local_time_to_display}")