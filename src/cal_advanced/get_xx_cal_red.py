import calendar
import sys
from colorama import Fore, Style, init

class CustomTextCalendar(calendar.TextCalendar):
    def __init__(self, custom_day, firstweekday=0):
        super().__init__(firstweekday)
        self.custom_day = custom_day
        self.tag = 'XX'
        self.color = Fore.RED

    def formatday(self, day, weekday, width):
        """
        Returns a formatted day.
        """
        if day == 0:
            s = ''
        elif day == self.custom_day:
            s = set_color(day, Fore.RED)
        else:
            s = '%2i' % day  # right-align single-digit days
        return s.center(width)


def set_color(s, color):
    return f"{Style.BRIGHT}{color}{s}{Style.RESET_ALL}"

def get_xx_cal(nums):
    year, month, day = nums
    custom_text_cal = CustomTextCalendar(custom_day=day)
    return custom_text_cal.formatmonth(year, month)


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    nums = read_input()
    print(get_xx_cal(nums))



if __name__ == "__main__":
    main()
