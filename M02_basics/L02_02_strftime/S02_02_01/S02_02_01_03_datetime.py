from datetime import datetime

dt = datetime(2025, 9, 25, 15, 30, 5)

# Пример 1: Формат, принятый в России (ДД.ММ.ГГГГ)
format_ru = dt.strftime("%d.%m.%Y")
print(f"Российский формат: {format_ru}")

# Пример 2: Формат для США (MM/DD/YY)
format_us = dt.strftime("%m/%d/%y")
print(f"Американский формат: {format_us}")

# Пример 3: Текстовое представление с днем недели
format_full = dt.strftime("%A, %d %B %Y года, %H:%M")
print(f"Полный формат: {format_full}")

# Пример 4: Формат для имен файлов или логов (сортируемый)
format_log = dt.strftime("%Y-%m-%d_%H-%M-%S")
print(f"Формат для логов: {format_log}")