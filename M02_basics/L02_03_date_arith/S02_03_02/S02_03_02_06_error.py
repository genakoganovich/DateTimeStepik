from datetime import datetime

dt1 = datetime(2025, 1, 1)
dt2 = datetime(2026, 1, 1)

try:
    result = dt1 + dt2
except TypeError as e:
    print(f"Ошибка: {e}")