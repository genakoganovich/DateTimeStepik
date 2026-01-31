from datetime import datetime


def get_month(date_string):
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%B")


def read_input():
    return input()


def main():
    date_string = read_input()
    print(get_month(date_string))


if __name__ == "__main__":
    main()
