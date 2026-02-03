import calendar
import sys

def is_working_day(day_date, month):
    return day_date.month == month and day_date.weekday() not in (calendar.SATURDAY, calendar.SUNDAY)

def get_total_work_days(nums):
    year, month = nums
    cal = calendar.Calendar()
    dates_iterator = cal.itermonthdates(year, month)
    total_work_days = sum(1 for day_date in dates_iterator if is_working_day(day_date, month))
    return total_work_days


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    nums = read_input()
    print(get_total_work_days(nums))

if __name__ == "__main__":
    main()
