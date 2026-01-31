from datetime import date


def create_date(year, month, day):
    return date(year, month, day)


def read_input():
    year = int(input())
    month = int(input())
    day = int(input())
    return year, month, day


def main():
    year, month, day = read_input()
    print(create_date(year, month, day))


if __name__ == "__main__":
    main()
