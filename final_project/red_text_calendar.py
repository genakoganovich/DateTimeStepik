import calendar
from colorama import Fore

from final_project.utils import Utils


class RedTextCalendar(calendar.TextCalendar):
    COLOR = Fore.RED

    def __init__(self, firstweekday=0):
        super().__init__(firstweekday)
        self.red_days = []


    def formatday(self, day, weekday, width):
        """
        Returns a formatted day.
        """
        if day == 0:
            s = ''
        elif day in self.red_days:
            s = Utils.set_color(day, self.COLOR)
        else:
            s = '%2i' % day  # right-align single-digit days
        return s.center(width)

    def set_red_days(self, red_days):
        self.red_days = red_days

    def reset_red_days(self):
        self.red_days = []