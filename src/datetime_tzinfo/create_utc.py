from datetime import datetime, timezone


def create_dt_utc(year, month, day, hours, minutes):
    dt = datetime(year, month, day, hours, minutes, tzinfo=timezone.utc)
    return dt


def read_input():
    return map(int, input().split())


def main():
    year, month, day, hours, minutes = read_input()
    print(create_dt_utc(year, month, day, hours, minutes))

if __name__ == "__main__":
    main()
