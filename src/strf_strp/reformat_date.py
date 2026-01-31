from datetime import datetime


def reformat_date(dt_string, dt_format_in, dt_format_out):
    dt = datetime.strptime(dt_string, dt_format_in)
    return dt.strftime(dt_format_out)


def read_input():
    return input()


def main():
    dt_string = read_input()
    dt_format_in = "%m/%d/%Y"
    dt_format_out = "%Y-%m-%d"
    print(reformat_date(dt_string, dt_format_in, dt_format_out))


if __name__ == "__main__":
    main()
