from datetime import date, time, datetime

start_work = time(9, 0)   # 09:00
end_work = time(18, 30)   # 18:30

# 1. Получаем условную дату (пусть будет "сегодня")
today = date.today()

# 2. Создаем полные объекты datetime
dt_start = datetime.combine(today, start_work)
dt_end = datetime.combine(today, end_work)

# 3. Теперь вычитание работает!
duration = dt_end - dt_start

print(f"Рабочий день длился: {duration}")
# Вывод: Рабочий день длился: 9:30:00
print(type(duration))
# Вывод: <class 'datetime.timedelta'>