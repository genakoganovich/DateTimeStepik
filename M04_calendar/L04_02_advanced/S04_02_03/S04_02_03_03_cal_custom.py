import calendar

year = 2025
month = 12

cal = calendar.Calendar()
dates_iterator = cal.itermonthdates(year, month)

print(f"--- Кастомный календарь на {month}/{year} ---")
print("Пн Вт Ср Чт Пт *Сб* *Вс*")

for day_date in dates_iterator:
    day_number = day_date.day

    # Если день относится к другому месяцу, выводим пустое место
    if day_date.month != month:
        print("  ", end=" ")
    else:
        # Проверяем на выходные
        is_weekend = day_date.weekday() in (calendar.SATURDAY, calendar.SUNDAY)
        # Форматируем строку (выравнивание + звездочка)
        print(f"{day_number: >2}{'*' if is_weekend else ' '}", end=" ")

    # Перенос строки в конце недели (в Воскресенье)
    if day_date.weekday() == calendar.SUNDAY:
        print()