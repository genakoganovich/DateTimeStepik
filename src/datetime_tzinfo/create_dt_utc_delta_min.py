from datetime import datetime, timedelta, timezone
from itertools import islice
import sys


def create_dt_utc_delta_min(numbers, offset):
    dt_offset = timedelta(minutes=offset)
    dt_tz = timezone(dt_offset)
    dt = datetime(*numbers, tzinfo=dt_tz)
    utc_offset = dt.utcoffset()
    utc_offset_minutes = int(utc_offset.total_seconds() // 60)
    utc_offset_sign = '+' if utc_offset_minutes >= 0 else '-'
    utc_offset_hours, utc_offset_minutes = divmod(abs(utc_offset_minutes), 60)
    return f"{dt:%Y-%m-%d %H:%M} [UTC{utc_offset_sign}{utc_offset_hours:02d}:{utc_offset_minutes:02d}]"


def read_input():
    numbers = [int(n) for line in islice(sys.stdin, 3) for n in line.split()]
    return numbers


def main():
    *numbers, offset = read_input()
    print(create_dt_utc_delta_min(numbers, offset))

if __name__ == "__main__":
    main()
