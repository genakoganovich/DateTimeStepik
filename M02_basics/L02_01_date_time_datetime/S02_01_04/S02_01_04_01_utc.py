from datetime import datetime, timezone, timedelta

# 1. НЕПРАВИЛЬНО для веб-сервисов
# Берет время сервера (зависит от того, где стоит компьютер)
local_server_time = datetime.now()
print(f"Опасное время: {local_server_time}")
# Вывод: 2023-10-05 15:30:00 (Например) - и мы не знаем, какой это пояс!


# 2. ПРАВИЛЬНО (Профессиональный стандарт)
# Всегда получаем точное время по UTC
utc_time = datetime.now(timezone.utc)
print(f"Надежное время (UTC): {utc_time}")
# Вывод: 2023-10-05 12:30:00+00:00 - четко видно, что это эталон.


# 3. Как показать пользователю (Пример)
# Допустим, мы знаем, что пользователь из Москвы (UTC+3)
moscow_offset = timezone(timedelta(hours=3))
user_time = utc_time.astimezone(moscow_offset)

print(f"Время для пользователя из Москвы: {user_time}")
# Вывод: 2023-10-05 15:30:00+03:00