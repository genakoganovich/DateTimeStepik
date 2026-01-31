from datetime import datetime, timedelta

now = datetime.now()
past_interval = timedelta(days=1000)

past_time = now - past_interval

print(f"Сейчас: {now.date()}")
print(f"1000 дней назад: {past_time.date()}")