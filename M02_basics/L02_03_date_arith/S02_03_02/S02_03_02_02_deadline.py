from datetime import datetime, timedelta

creation_time = datetime.now()
deadline_interval = timedelta(days=3, hours=12)

deadline = creation_time + deadline_interval

print(f"Задача создана:  {creation_time.strftime('%Y-%m-%d %H:%M')}")
print(f"Срок выполнения: {deadline.strftime('%Y-%m-%d %H:%M')}")