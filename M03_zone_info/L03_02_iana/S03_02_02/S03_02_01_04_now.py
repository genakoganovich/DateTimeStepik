from datetime import datetime
from zoneinfo import ZoneInfo

# Получение текущего времени в Токио
tokyo_tz = ZoneInfo("Asia/Tokyo")
now_in_tokyo = datetime.now(tokyo_tz)

print(f"Текущее время в Токио: {now_in_tokyo}")