from datetime import datetime, timezone, timedelta

# 1. Создание осведомленного объекта в UTC
# Это стандартный и рекомендуемый способ
utc_time = datetime(2025, 9, 25, 12, 0, 0, tzinfo=timezone.utc)

print(f"Время в UTC: {utc_time}")
print(f"Объект tzinfo: {utc_time.tzinfo}")
print(f"Смещение от UTC: {utc_time.utcoffset()}")