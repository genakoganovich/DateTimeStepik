from datetime import timedelta

delta = timedelta(days=1, hours=1)

# Сравним атрибуты и метод
print(f"Атрибут .days: {delta.days}")
print(f"Атрибут .seconds: {delta.seconds}")
print(f"Метод .total_seconds(): {delta.total_seconds()}")