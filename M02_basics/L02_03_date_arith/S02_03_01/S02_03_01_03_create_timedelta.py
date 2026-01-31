from datetime import timedelta

# Интервал в 7 дней (одна неделя)
delta1 = timedelta(days=7)
print(f"Интервал 1: {delta1}")

# Интервал в 2 часа 30 минут
delta2 = timedelta(hours=2, minutes=30)
print(f"Интервал 2: {delta2}")

# Интервал может быть и отрицательным
delta3 = timedelta(days=-1)
print(f"Интервал 3: {delta3}")

# Более сложный интервал
delta4 = timedelta(weeks=2, days=3, hours=4, minutes=5, seconds=6)
print(f"Интервал 4: {delta4}")