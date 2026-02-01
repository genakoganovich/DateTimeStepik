from datetime import datetime

# Создаем наивный объект
naive_dt = datetime(2025, 9, 25, 15, 30)

print(f"Объект: {naive_dt}")
print(f"Атрибут tzinfo: {naive_dt.tzinfo}")
print(f"Является ли объект наивным? {naive_dt.tzinfo is None}")