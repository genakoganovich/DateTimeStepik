from datetime import datetime, timedelta


def get_rocket_signal_dt(dt_string, hour, minute, second, dt_output_format):
    dt = datetime.fromisoformat(dt_string)
    delta = timedelta(hours=hour, minutes=minute, seconds=second)
    dt_signal = dt - delta
    return dt_signal.strftime(dt_output_format)


def read_dt_string():
    return input()


def read_delta_string():
    return map(int, input().split())


def main():
    dt_output_format = "%Y-%m-%d %H:%M:%S"
    dt_string = read_dt_string()
    hour, minute, second = read_delta_string()
    print(get_rocket_signal_dt(dt_string, hour, minute, second, dt_output_format))


if __name__ == "__main__":
    main()
