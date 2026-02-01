from datetime import datetime


def check_naive(dt_string):

    dt = datetime.strptime(dt_string, "%Y %m %d")
    return "Aware" if dt.tzinfo else "Naive"



def read_input():
    return input()


def main():
    dt_string = read_input()
    print(check_naive(dt_string))

if __name__ == "__main__":
    main()
