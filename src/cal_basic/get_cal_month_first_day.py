from enum import Enum
import calendar


class Weekday(Enum):
    SUN = calendar.SUNDAY
    MON = calendar.MONDAY
    TUE = calendar.TUESDAY
    WED = calendar.WEDNESDAY
    THU = calendar.THURSDAY
    FRI = calendar.FRIDAY
    SAT = calendar.SATURDAY

    @classmethod
    def from_str(cls, value: str) -> "Weekday":
        try:
            return cls[value.upper()]
        except KeyError:
            raise ValueError(f"Invalid weekday: {value!r}")

def get_cal_month_first_day(nums, first_weekday):

    weekday = Weekday.from_str(first_weekday)
    cal_obj = calendar.TextCalendar(firstweekday=weekday.value)
    return cal_obj.formatmonth(*nums)


def read_input():
    nums = map(int, input().split())
    first_weekday = input()
    return nums, first_weekday

def main():
    nums, first_weekday = read_input()
    print(get_cal_month_first_day(nums, first_weekday))

if __name__ == "__main__":
    main()
