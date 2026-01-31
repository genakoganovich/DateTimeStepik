from datetime import time

t = time(14, 30, 5, 123456)

print(f"Час: {t.hour}")
print(f"Минута: {t.minute}")
print(f"Секунда: {t.second}")
print(f"Микросекунда: {t.microsecond}")

# Вывод:
# Час: 14
# Минута: 30
# Секунда: 5
# Микросекунда: 123456