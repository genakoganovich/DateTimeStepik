import calendar


def count_full_weeks(nums):
    matrix = calendar.monthcalendar(*nums)
    week_count = sum(all(x != 0 for x in week) for week in matrix)
    return week_count


def read_input():
    return map(int, input().split())


def main():
    nums = read_input()
    print(count_full_weeks(nums))

if __name__ == "__main__":
    main()
