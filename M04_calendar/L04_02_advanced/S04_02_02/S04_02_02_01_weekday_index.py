import calendar

year = 2025
month = 9
day = 1

day_index = calendar.weekday(year, month, day)

print(f"Индекс дня недели для {day}.{month}.{year}: {day_index}")
print(f"Этот индекс соответствует константе MONDAY: {day_index == calendar.MONDAY}")