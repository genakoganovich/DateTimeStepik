from datetime import date, time, datetime


def combine_datetime(d_nums, t_nums):
    user_date = date(*d_nums)
    user_time = time(*t_nums)
    return datetime.combine(user_date, user_time)


def read_input():
    return map(int, input().split())


def main():
    d_nums = read_input()
    t_nums = read_input()
    print(combine_datetime(d_nums, t_nums))


if __name__ == "__main__":
    main()
