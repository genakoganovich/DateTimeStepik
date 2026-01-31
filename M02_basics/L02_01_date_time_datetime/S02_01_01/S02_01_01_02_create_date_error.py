from datetime import date

try:
    invalid_date = date(2025, 2, 30)
except ValueError as e:
    print(e)
