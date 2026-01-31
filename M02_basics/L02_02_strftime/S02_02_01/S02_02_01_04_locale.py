import locale
from datetime import datetime

# Устанавливаем русскую локаль.
# Название локали может отличаться в разных ОС ('ru_RU.UTF-8', 'russian')
try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except locale.Error:
    print("Локаль 'ru_RU.UTF-8' не поддерживается в вашей системе.")
    # Попробуйте 'rus_rus' для Windows

dt = datetime(2025, 9, 25, 15, 30, 5)

# Тот же формат, что и в примере 3
format_full_ru = dt.strftime("%A, %d %B %Y года")
print(f"Полный формат (RU): {format_full_ru}")