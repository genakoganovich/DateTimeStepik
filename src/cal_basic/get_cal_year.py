import calendar


def get_cal_year(year, n_col):
    return calendar.calendar(year, m=n_col)


def read_input():
    return int(input())


def main():
    year = read_input()
    n_col = 2
    print(get_cal_year(year, n_col))


if __name__ == "__main__":
    main()
