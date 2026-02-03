import calendar
import sys


def get_last_tuesday(nums):
    year, month = nums
    matrix = calendar.monthcalendar(year, month)
    for week in reversed(matrix):
        for day in week:
            if day != 0 and calendar.weekday(year, month, day) == calendar.TUESDAY:
                return day
    return 0


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    nums = read_input()
    print(get_last_tuesday(nums))

if __name__ == "__main__":
    main()
