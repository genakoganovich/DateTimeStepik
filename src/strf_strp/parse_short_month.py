from datetime import datetime


def parse_short_month(dt_string, dt_format):
    dt = datetime.strptime(dt_string, dt_format)
    return dt.hour


def read_input():
    return input()


def main():
    dt_format = "%d-%b-%Y %H:%M:%S"
    dt_string = read_input()
    print(parse_short_month(dt_string, dt_format))

if __name__ == "__main__":
    main()
