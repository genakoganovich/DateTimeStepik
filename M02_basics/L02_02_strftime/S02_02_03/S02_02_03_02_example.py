from datetime import datetime

# Пример 1: Стандартный формат даты
date_str_1 = "2025-09-25"
format_1 = "%Y-%m-%d"
dt_obj_1 = datetime.strptime(date_str_1, format_1)
print(f"Строка: '{date_str_1}' -> Объект: {dt_obj_1}")
print(f"Тип объекта: {type(dt_obj_1)}")

# Пример 2: Нестандартный европейский формат с временем
date_str_2 = "25.09.2025 15:30"
format_2 = "%d.%m.%Y %H:%M"
dt_obj_2 = datetime.strptime(date_str_2, format_2)
print(f"Строка: '{date_str_2}' -> Объект: {dt_obj_2}")

# Пример 3: Текстовый формат с названием месяца
date_str_3 = "September 25, 2025"
format_3 = "%B %d, %Y"
dt_obj_3 = datetime.strptime(date_str_3, format_3)
print(f"Строка: '{date_str_3}' -> Объект: {dt_obj_3}")