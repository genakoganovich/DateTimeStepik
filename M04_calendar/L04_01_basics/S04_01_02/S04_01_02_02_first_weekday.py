import calendar

# --- Вывод по умолчанию ---
print("--- Стандартный вывод (неделя с Понедельника) ---")
print(calendar.month(2025, 9))

# --- Меняем первый день недели на Воскресенье ---
calendar.setfirstweekday(calendar.SUNDAY)

# --- Вывод после изменения настройки ---
print("--- Неделя с Воскресенья ---")
print(calendar.month(2025, 9))