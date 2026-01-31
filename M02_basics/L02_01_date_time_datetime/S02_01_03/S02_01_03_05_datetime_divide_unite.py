from datetime import date, datetime, time

dt = datetime(2025, 9, 25, 15, 30)

# 1. Разделение
date_part = dt.date()
time_part = dt.time()

print(f"Объект date: {date_part}")
print(f"Объект time: {time_part}")

# 2. Объединение
d = date(2026, 1, 1)
t = time(0, 0)
new_year_datetime = datetime.combine(d, t)

print(f"Объединенный объект: {new_year_datetime}")

# Вывод:
# Объект date: 2025-09-25
# Объект time: 15:30:00
# Объединенный объект: 2026-01-01 00:00:00