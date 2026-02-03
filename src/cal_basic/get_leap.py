import calendar


def get_leap(year):
    return "LEAP" if calendar.isleap(year) else "COMMON"


def read_input():
    return int(input())


def main():
    year = read_input()
    print(get_leap(year))

if __name__ == "__main__":
    main()
