import calendar
import sys


def is_friday_13(nums, day):
    return calendar.weekday(*nums, day) == calendar.FRIDAY


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    day = 13
    nums = read_input()
    print(is_friday_13(nums, day))


if __name__ == "__main__":
    main()
