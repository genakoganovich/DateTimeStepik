from datetime import time

def set_alarm_clock(hour, minute, second):
    return time(hour, minute, second)


def read_input():
    hour = int(input())
    minute = int(input())
    second = int(input())
    return hour, minute, second

def main():
    hour, minute, second = read_input()
    print(set_alarm_clock(hour, minute, second))

if __name__ == "__main__":
    main()
