from datetime import datetime, timedelta, timezone
from itertools import islice
import sys



def create_dt_utc_delta(numbers, offset):
    dt_offset = timedelta(hours=offset)
    dt_tz = timezone(dt_offset)
    dt = datetime(*numbers, tzinfo=dt_tz)
    return dt


def read_input():
    numbers = [int(n) for line in islice(sys.stdin, 3) for n in line.split()]
    return numbers

def main():
    *numbers, offset = read_input()
    print(create_dt_utc_delta(numbers, offset))

if __name__ == "__main__":
    main()
