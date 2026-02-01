from datetime import datetime
from zoneinfo import ZoneInfo


def create_aware(nums, src_tz_string, target):
    src_tz = ZoneInfo(src_tz_string)
    src_dt = datetime(*nums, tzinfo=src_tz)

    res = list()
    for target_city, target_tz in target:
        target_dt = src_dt.astimezone(ZoneInfo(target_tz))
        res.append(f"{target_city}: {target_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    return "\n".join(res)


def read_input():
    nums = map(int, input().split())
    tz_string = input()
    return nums, tz_string


def main():
    target = [('Лондон', 'Europe/London'),
              ('Москва', 'Europe/Moscow'),
              ('Токио', 'Asia/Tokyo')
    ]

    nums, tz_string = read_input()
    print(create_aware(nums, tz_string, target))

if __name__ == "__main__":
    main()
