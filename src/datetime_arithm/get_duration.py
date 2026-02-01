from datetime import date, time, datetime


def get_duration(t_beg_string, t_end_string):
    t_beg = time.fromisoformat(t_beg_string)
    t_end = time.fromisoformat(t_end_string)
    today = date.today()
    dt_beg = datetime.combine(today, t_beg)
    dt_end = datetime.combine(today, t_end)
    return (dt_end - dt_beg).seconds // 60


def read_input():
    return [input() for _ in range(2)]


def main():
    t_strings = read_input()
    print(get_duration(*t_strings))


if __name__ == "__main__":
    main()
