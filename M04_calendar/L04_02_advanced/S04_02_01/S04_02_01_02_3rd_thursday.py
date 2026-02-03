import calendar

year = 2025
month = 9
matrix = calendar.monthcalendar(year, month)

# Ищем 3-й четверг (THURSDAY, индекс 3)
target_weekday = calendar.THURSDAY  # = 3
target_occurrence = 3

thursday_count = 0
third_thursday_date = None

for week in matrix:
    # Проверяем, есть ли в этой неделе четверг, принадлежащий этому месяцу
    if week[target_weekday] != 0:
        thursday_count += 1
        if thursday_count == target_occurrence:
            third_thursday_date = week[target_weekday]
            break # Нашли, можно выходить из цикла

if third_thursday_date:
    print(f"Третий четверг в {month}/{year} - это {third_thursday_date} число.")
else:
    print(f"В {month}/{year} нет третьего четверга.")