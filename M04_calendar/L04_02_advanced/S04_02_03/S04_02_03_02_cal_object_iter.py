import calendar

cal = calendar.Calendar(firstweekday=calendar.MONDAY) # Начнем с понедельника для наглядности

# Получаем итератор для февраля 2026
dates_iterator = cal.itermonthdates(2026, 2)

print("Даты из итератора для Февраля 2026 (начало недели - Пн):")
# Преобразуем итератор в список, чтобы вывести все сразу
# all_dates = list(dates_iterator)
for day_date in dates_iterator:
    print(day_date)