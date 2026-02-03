import calendar

# Создаем кортеж с названиями дней недели (индексы 0-6)
# Важно, чтобы порядок соответствовал нумерации calendar
weekday_names = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

year = 2026
month = 1
day = 1

# Определяем индекс
day_index = calendar.weekday(year, month, day)

# Используем индекс для получения названия из нашего кортежа
day_name = weekday_names[day_index]

print(f"{day}.{month}.{year} - это {day_name}.")