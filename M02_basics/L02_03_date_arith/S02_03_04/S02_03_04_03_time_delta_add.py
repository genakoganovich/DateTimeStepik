from datetime import datetime, date, time, timedelta

current_time = time(23, 0) # 23:00

# Хотим узнать, сколько будет времени через 2 часа
# 1. Превращаем в datetime
dt_current = datetime.combine(date.today(), current_time)

# 2. Прибавляем timedelta
dt_future = dt_current + timedelta(hours=2)

# 3. Извлекаем обратно только время
future_time = dt_future.time()

print(future_time)
# Вывод: 01:00:00