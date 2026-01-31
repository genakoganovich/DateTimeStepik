from datetime import date, time, datetime


def combine_datetime(year, month, day, hour, minute):
    user_date = date(year, month, day)
    user_time = time(hour, minute)
    return datetime.combine(user_date, user_time)


def read_input():
    return map(int, input().split())


def main():
    year, month, day = read_input()
    hour, minute = read_input()
    print(combine_datetime(year, month, day, hour, minute))


if __name__ == "__main__":
    main()
