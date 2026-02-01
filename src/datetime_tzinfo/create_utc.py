from datetime import datetime, timezone


def create_dt_utc(numbers):
    dt = datetime(*numbers, tzinfo=timezone.utc)
    return dt


def read_input():
    return map(int, input().split())


def main():
    numbers = read_input()
    print(create_dt_utc(numbers))

if __name__ == "__main__":
    main()
