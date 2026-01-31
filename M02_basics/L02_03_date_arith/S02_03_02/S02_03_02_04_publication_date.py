from datetime import datetime, timedelta

current_time = datetime.now()
time_since_publication = timedelta(hours=8, minutes=45)

publication_time = current_time - time_since_publication

print(f"Время проверки:    {current_time.strftime('%H:%M:%S')}")
print(f"Время публикации:  {publication_time.strftime('%H:%M:%S')}")