from datetime import datetime, timezone, timedelta

# Создадим "осведомленный" объект для демонстрации директив часового пояса
tz_msk = timezone(timedelta(hours=3), name="MSK")
aware_dt = datetime(2025, 9, 25, 15, 30, 5, 123456, tzinfo=tz_msk)

# День года и номер недели
print(aware_dt.strftime("Сегодня %j-й день %Y года."))
print(aware_dt.strftime("Неделя %U (начало в Вс), Неделя %W (начало в Пн)."))

# 12-часовой формат времени
print(aware_dt.strftime("Время: %I:%M:%S %p"))

# Информация о часовом поясе
print(aware_dt.strftime("Часовой пояс: %Z, смещение: %z"))

# Локализованный формат
print(aware_dt.strftime("Локальный формат даты и времени: %c"))