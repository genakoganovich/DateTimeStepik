from datetime import datetime

def create_logfile_name(dt_string, dt_format):
    dt = datetime.strptime(dt_string, dt_format)
    return dt.strftime("%Y-%m-%d_%H-%M-%S")


def read_input():
    return input()

def main():
    dt_format = "%Y %m %d %H %M %S"
    dt_string = read_input()
    print(create_logfile_name(dt_string, dt_format))

if __name__ == "__main__":
    main()
