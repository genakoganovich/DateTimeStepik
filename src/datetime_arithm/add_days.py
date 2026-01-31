from datetime import datetime, timedelta


def add_days(dt_string, n, dt_format_out):
    dt = datetime.fromisoformat(dt_string)
    days_delta = timedelta(days=n)
    return (dt + days_delta).strftime(dt_format_out)


def read_input():
    dt_string = input()
    n = int(input())
    return dt_string, n


def main():
    dt_format_out = "%Y-%m-%d"
    dt_string, n = read_input()
    print(add_days(dt_string, n, dt_format_out))


if __name__ == "__main__":
    main()
