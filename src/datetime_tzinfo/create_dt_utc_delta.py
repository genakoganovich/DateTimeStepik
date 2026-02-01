from datetime import datetime, timedelta, timezone


def create_dt_utc_delta(year, month, day, hour, minute, offset):
    dt_offset = timedelta(hours=offset)
    dt_tz = timezone(dt_offset)
    dt = datetime(year, month, day, hour, minute, tzinfo=dt_tz)
    return dt


def read_input():
    year, month, day = map(int, input().split())
    hour, minute, = map(int, input().split())
    offset = int(input())
    return year, month, day, hour, minute, offset


def main():
    year, month, day, hour, minute, offset = read_input()
    print(create_dt_utc_delta(year, month, day, hour, minute, offset))

if __name__ == "__main__":
    main()
