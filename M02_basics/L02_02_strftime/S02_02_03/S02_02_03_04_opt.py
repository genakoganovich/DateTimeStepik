from datetime import datetime

iso_date_str = "2025-09-25T15:30:05.123456"
dt_obj = datetime.fromisoformat(iso_date_str)

print(dt_obj)
# Вывод: 2025-09-25 15:30:05.123456