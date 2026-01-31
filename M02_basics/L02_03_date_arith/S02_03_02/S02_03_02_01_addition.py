from datetime import datetime, timedelta

start_time = datetime(2025, 10, 1, 12, 0, 0)
# Увеличиваем интервал, чтобы выйти за пределы октября
interval = timedelta(days=40, hours=4)

future_time = start_time + interval

print(f"Начальная точка: {start_time}")
print(f"Будущая точка:   {future_time}")