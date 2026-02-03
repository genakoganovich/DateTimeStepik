import calendar

# Получаем матрицу календаря
sept_2025_matrix = calendar.monthcalendar(2025, 9)

print("Матрица для Сентября 2025:")
# Выведем для наглядности каждую неделю на новой строке
for week in sept_2025_matrix:
    print(week)