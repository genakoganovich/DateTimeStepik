from datetime import datetime

start_webinar = datetime(2025, 9, 25, 18, 0, 0)
end_webinar = datetime(2025, 9, 25, 19, 35, 15)

# Продолжим предыдущий пример
duration = end_webinar - start_webinar

# Используем .total_seconds() для получения общей длительности в секундах
total_seconds = duration.total_seconds()
print(f"Общая длительность в секундах: {total_seconds}")

# На основе этого можно вычислить длительность в других единицах
total_minutes = total_seconds / 60
print(f"Общая длительность в минутах: {total_minutes}")