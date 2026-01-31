from datetime import time

try:
    invalid_time = time(25, 0)
except ValueError as e:
    print(e)

# Вывод: hour must be in 0..23