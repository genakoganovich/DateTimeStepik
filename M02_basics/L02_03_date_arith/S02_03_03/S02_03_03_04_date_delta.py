from datetime import date

birth_date = date(1990, 5, 15)
current_date = date.today()

age_in_days = current_date - birth_date

print(f"Дата рождения: {birth_date}")
print(f"Текущая дата: {current_date}")
print(f"Возраст в днях: {age_in_days}")
print(f"Только дни: {age_in_days.days}")