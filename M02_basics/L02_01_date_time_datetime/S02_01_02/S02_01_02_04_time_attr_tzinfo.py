from datetime import time
from datetime import timezone

# "Наивное" время (tzinfo is None)
naive_time = time(14, 30)
print(f"Наивное время: {naive_time}, tzinfo: {naive_time.tzinfo}")

# "Осведомленное" время (с указанием UTC)
# Подробно работу с timezone мы изучим в следующем модуле
aware_time = time(14, 30, tzinfo=timezone.utc)
print(f"Осведомленное время: {aware_time}, tzinfo: {aware_time.tzinfo}")

# Вывод:
# Наивное время: 14:30:00, tzinfo: None
# Осведомленное время: 14:30:00+00:00, tzinfo: UTC