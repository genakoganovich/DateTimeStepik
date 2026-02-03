import calendar


def get_leap_range(first_year, last_year):
    leap_years = [str(year) for year in range(first_year, last_year + 1) if calendar.isleap(year)]
    return "\n".join(leap_years)


def read_input():
    return map(int, input().split())

def main():
    nums = read_input()
    print(get_leap_range(*nums))

if __name__ == "__main__":
    main()
