from datetime import datetime, timezone

# Создаем осведомленный объект для времени в UTC
aware_dt = datetime(2025, 9, 25, 15, 30, tzinfo=timezone.utc)

print(f"Объект: {aware_dt}")
print(f"Атрибут tzinfo: {aware_dt.tzinfo}")
print(f"Является ли объект наивным? {aware_dt.tzinfo is None}")