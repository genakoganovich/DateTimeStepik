from datetime import timedelta

# 25 часов = 1 день и 1 час (3600 секунд)
delta = timedelta(hours=25)

print(f"Объект timedelta: {delta}")
print(f"Атрибут .days: {delta.days}")
print(f"Атрибут .seconds: {delta.seconds}")