import calendar


def get_cal_month(nums):
    return calendar.month(*nums)


def read_input():
    return map(int, input().split())

def main():
    nums = read_input()
    print(get_cal_month(nums))

if __name__ == "__main__":
    main()
