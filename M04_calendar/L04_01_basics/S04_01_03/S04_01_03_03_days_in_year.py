import calendar

def days_in_year(year):
    """Возвращает количество дней в указанном году."""
    if calendar.isleap(year):
        return 366
    else:
        return 365

# Используем нашу функцию
year_to_check = 2024
print(f"В {year_to_check} году {days_in_year(year_to_check)} дней.")

year_to_check = 2025
print(f"В {year_to_check} году {days_in_year(year_to_check)} дней.")