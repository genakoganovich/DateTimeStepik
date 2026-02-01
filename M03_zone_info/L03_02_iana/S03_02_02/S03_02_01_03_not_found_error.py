from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

try:
    invalid_tz = ZoneInfo("Europe/MySuperCity")
except ZoneInfoNotFoundError as e:
    print(f"Ошибка: {e}")