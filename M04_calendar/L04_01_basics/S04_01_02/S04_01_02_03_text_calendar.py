import calendar

# Создаем объект Текстового Календаря, где неделя начинается с Воскресенья.
# Эта настройка локальна только для объекта 'cal_obj'.
cal_obj = calendar.TextCalendar(firstweekday=calendar.SUNDAY)

# Используем метод объекта .formatmonth() для генерации строки
print(cal_obj.formatmonth(2025, 9))