from datetime import datetime
from zoneinfo import ZoneInfo


def make_aware(nums, source_iana_id, target_iana_id):
    source_naive_dt = datetime(*nums)
    source_aware_dt = source_naive_dt.replace(tzinfo=ZoneInfo(source_iana_id))
    target_dt = source_aware_dt.astimezone(ZoneInfo(target_iana_id))
    return target_dt


def read_input():
    nums = map(int, input().split())
    source_iana_id = input()
    target_iana_id = input()
    return nums, source_iana_id, target_iana_id


def main():
    nums, source_iana_id, target_iana_id = read_input()
    print(make_aware(nums, source_iana_id, target_iana_id))

if __name__ == "__main__":
    main()
