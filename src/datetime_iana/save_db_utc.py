from datetime import datetime
from zoneinfo import ZoneInfo


def save_db_utc(nums, loca_tz_string):
    local_tz = ZoneInfo(loca_tz_string)
    local_dt = datetime(*nums, tzinfo=local_tz)
    utc_time_to_store = local_dt.astimezone(ZoneInfo('UTC'))
    return utc_time_to_store.strftime('%Y-%m-%d %H:%M:%S')


def read_input():
    nums = map(int, input().split())
    tz_string = input()
    return nums, tz_string


def main():
    nums, loca_tz_string = read_input()
    print(save_db_utc(nums, loca_tz_string))

if __name__ == "__main__":
    main()
