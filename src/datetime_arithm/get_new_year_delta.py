from datetime import datetime, timedelta


def get_new_year_delta(dt_string):
    dt = datetime.fromisoformat(dt_string)
    dt_new_year = datetime(year=dt.year + 1, month=1, day=1)
    return (dt_new_year - dt).days


def read_input():
    return input()

def main():
    dt_string = read_input()
    print(get_new_year_delta(dt_string))

if __name__ == "__main__":
    main()
