from datetime import datetime

def get_datetime_attr(year, month, day, hours, minutes, seconds):
    user_datetime = datetime(year, month, day, hours, minutes, seconds)
    return f"Дата: {user_datetime.date()}\nВремя: {user_datetime.time()}"


def read_input():
    return map(int, input().split())


def main():
    year, month, day, hours, minutes, seconds = read_input()
    print(get_datetime_attr(year, month, day, hours, minutes, seconds))

if __name__ == "__main__":
    main()
