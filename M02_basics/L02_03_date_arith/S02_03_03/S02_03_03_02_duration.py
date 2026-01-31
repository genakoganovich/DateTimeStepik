from datetime import datetime

start_webinar = datetime(2025, 9, 25, 18, 0, 0)
end_webinar = datetime(2025, 9, 25, 19, 35, 15)

# Вычитаем из времени окончания время начала
duration = end_webinar - start_webinar

print(f"Результат вычитания: {duration}")
print(f"Тип результата: {type(duration)}")