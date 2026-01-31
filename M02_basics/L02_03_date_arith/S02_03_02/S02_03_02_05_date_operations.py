from datetime import date, timedelta

start_date = date.today()
thirty_days = timedelta(days=30)

# Срок годности продукта - 30 дней
expiry_date = start_date + thirty_days
print(f"Дата производства: {start_date}")
print(f"Срок годности до:  {expiry_date}")