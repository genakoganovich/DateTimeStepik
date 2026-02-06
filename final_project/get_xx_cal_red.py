import sys

from final_project.red_text_calendar import RedTextCalendar


def get_xx_cal(nums):
    year, month, day = nums
    red_text_cal = RedTextCalendar()
    return red_text_cal.formatmonth(year, month)


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    nums = read_input()
    print(get_xx_cal(nums))



if __name__ == "__main__":
    main()
