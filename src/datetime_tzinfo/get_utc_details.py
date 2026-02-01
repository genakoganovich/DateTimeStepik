from datetime import datetime


def get_utc_details(dt_string):
    dt = datetime.fromisoformat(dt_string)
    return f"{dt.strftime('%H:%M:%S')}\n{dt.utcoffset()}"


def read_input():
    return input()


def main():
    dt_string = read_input()
    print(get_utc_details(dt_string))

if __name__ == "__main__":
    main()
