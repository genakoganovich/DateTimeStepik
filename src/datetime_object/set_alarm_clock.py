from datetime import time

def set_alarm_clock(nums):
    return time(*nums)


def read_input():
    return [int(input()) for _ in range(3)]

def main():
    nums = read_input()
    print(set_alarm_clock(nums))

if __name__ == "__main__":
    main()
