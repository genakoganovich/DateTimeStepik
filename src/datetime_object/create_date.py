from datetime import date


def create_date(nums):
    return date(*nums)


def read_input():
    return [int(input()) for _ in range(3)]


def main():
    nums = read_input()
    print(create_date(nums))


if __name__ == "__main__":
    main()
