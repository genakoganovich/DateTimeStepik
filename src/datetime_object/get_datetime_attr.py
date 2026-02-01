from datetime import datetime

def get_datetime_attr(nums):
    user_datetime = datetime(*nums)
    return f"Дата: {user_datetime.date()}\nВремя: {user_datetime.time()}"


def read_input():
    return map(int, input().split())


def main():
    nums = read_input()
    print(get_datetime_attr(nums))

if __name__ == "__main__":
    main()
