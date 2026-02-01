from datetime import datetime, timedelta, timezone


def create_dt_utc_delta_min(year, month, day, hour, minute, offset):
    dt_offset = timedelta(minutes=offset)
    dt_tz = timezone(dt_offset)
    dt = datetime(year, month, day, hour, minute, tzinfo=dt_tz)
    utc_offset = dt.utcoffset()
    utc_offset_minutes = int(utc_offset.total_seconds() // 60)
    utc_offset_sign = '+' if utc_offset_minutes >= 0 else '-'
    utc_offset_hours, utc_offset_minutes = divmod(abs(utc_offset_minutes), 60)
    return f"{dt:%Y-%m-%d %H:%M} [UTC{utc_offset_sign}{utc_offset_hours:02d}:{utc_offset_minutes:02d}]"


def read_input():
    year, month, day = map(int, input().split())
    hour, minute, = map(int, input().split())
    offset = int(input())
    return year, month, day, hour, minute, offset


def main():
    year, month, day, hour, minute, offset = read_input()
    print(create_dt_utc_delta_min(year, month, day, hour, minute, offset))

if __name__ == "__main__":
    main()
