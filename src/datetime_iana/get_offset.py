from datetime import datetime
from zoneinfo import ZoneInfo

def get_offset(iana_id):
    dt_january = datetime(datetime.now().year, 1, 15, tzinfo=ZoneInfo(iana_id))
    dt_july = datetime(datetime.now().year, 7, 15, tzinfo=ZoneInfo(iana_id))
    return f"{dt_january.utcoffset()}\n{dt_july.utcoffset()}"


def read_input():
    return input()


def main():
    iana_id = read_input()
    print(get_offset(iana_id))

if __name__ == "__main__":
    main()
