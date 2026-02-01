from datetime import datetime
from zoneinfo import ZoneInfo

# 1. Определяем исходное время встречи
la_tz = ZoneInfo("America/Los_Angeles")
meeting_time_la = datetime(2025, 11, 5, 9, 0, 0, tzinfo=la_tz)

print(f"Исходное время (Лос-Анджелес): {meeting_time_la}")
print("-" * 40)

# 2. Определяем целевые часовые пояса
london_tz = ZoneInfo("Europe/London")
tokyo_tz = ZoneInfo("Asia/Tokyo")

# 3. Выполняем преобразование
meeting_time_london = meeting_time_la.astimezone(london_tz)
meeting_time_tokyo = meeting_time_la.astimezone(tokyo_tz)

print(f"Время встречи в Лондоне:      {meeting_time_london}")
print(f"Время встречи в Токио:        {meeting_time_tokyo}")