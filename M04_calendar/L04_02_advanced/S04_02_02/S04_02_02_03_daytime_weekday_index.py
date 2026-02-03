from datetime import date
import calendar

year = 2025
month = 10
day = 31

# Способ 1: через calendar
index_from_calendar = calendar.weekday(year, month, day)
print(f"Результат calendar.weekday(): {index_from_calendar}")

# Способ 2: через объект date
d = date(year, month, day)
index_from_date = d.weekday()
print(f"Результат date.weekday():   {index_from_date}")