from datetime import timedelta


def get_total_duration(duration_values):
    total = sum((timedelta(**v) for v in duration_values), timedelta())
    return f"{total.days} {total.seconds}"


def read_input_line():
    return dict(zip(('days', 'hours', 'minutes'), map(int, input().split())))


def read_input():
    n = int(input())
    return [read_input_line() for _ in range(n)]


def main():
    duration_values = read_input()
    print(get_total_duration(duration_values))


if __name__ == "__main__":
    main()
