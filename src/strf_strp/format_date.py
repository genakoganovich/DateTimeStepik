from datetime import date

def format_date(year, month, day):
    dt = date(year, month, day)
    return dt.strftime('%d.%m.%Y')


def read_input():
    year = int(input())
    month = int(input())
    day = int(input())
    return year, month, day

def main():
    year, month, day = read_input()
    print(format_date(year, month, day))

if __name__ == "__main__":
    main()
