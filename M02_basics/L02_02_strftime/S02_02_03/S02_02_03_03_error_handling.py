from datetime import datetime

date_str = "25/09/2025"  # Разделитель - слэш
format_str = "%d.%m.%Y"  # А в формате ожидается точка

try:
    dt_obj = datetime.strptime(date_str, format_str)
except ValueError as e:
    print(f"Ошибка! Формат не соответствует строке.")
    print(f"Текст ошибки: {e}")

# Вывод:
# Ошибка! Формат не соответствует строке.
# Текст ошибки: time data '25/09/2025' does not match format '%d.%m.%Y'