import calendar
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import defaultdict

class EventStorage:
    def __init__(self):
        self.events = defaultdict(list)  # dt -> list[str]

    def add_event(self, date, title):
        self.events[date].append(title)

    def get_events(self, date):
        return self.events.get(date, [])


class CalendarApp:
    def __init__(self):
        self.storage = EventStorage()
        self.tz = ZoneInfo("UTC")
        self.commands = ["show <год> <месяц>",
                         "add",
                         "view <год> <месяц> <день>",
                         "help",
                         "exit"]

    def run(self):
        self.show_current_month()

        while True:
            try:
                command = input("> ").strip()
                if not command:
                    continue

                if command == "exit":
                    print("До свидания!")
                    break

                self.handle_command(command)

            except KeyboardInterrupt:
                print("\nИспользуйте команду 'exit' для выхода.")

    def handle_command(self, command: str):
        parts = command.split()
        cmd = parts[0]

        if cmd == "show":
            self.cmd_show(parts)
        elif cmd == "add":
            self.cmd_add()
        elif cmd == "view":
            self.cmd_view(parts)
        elif cmd == "help":
            self.cmd_help()
        else:
            print("Неизвестная команда")

    def cmd_show(self, parts):
        if len(parts) != 3:
            print("Использование: show <год> <месяц>")
            return

        year, month = map(int, parts[1:])
        self.show_month(year, month)

    def cmd_add(self):
        print("Добавление события")
        nums = tuple(map(int, input("Дата (YYYY MM DD): ").split()))
        date = datetime(*nums, tzinfo=self.tz)
        title = input("Название: ")

        self.storage.add_event(date, title)
        print("Событие добавлено")

    def cmd_view(self, parts):
        if len(parts) != 4:
            print("Использование: view <год> <месяц> <день>")
            return

        nums = map(int, parts[1:])
        date = datetime(*nums, tzinfo=self.tz)
        events = self.storage.get_events(date)

        if not events:
            print("Событий нет")
        else:
            for e in events:
                print("-", e)

    def cmd_help(self):
        print(self.commands)

    def cmd_unknown(self):
        print("Неизвестная команда")
        self.cmd_help()

    def show_current_month(self):
        now = datetime.now(self.tz)
        print(calendar.month(now.year, now.month))

    def show_month(self, year, month):
        print(calendar.month(year, month))



def main():
    calendar_app = CalendarApp()
    calendar_app.run()


if __name__ == "__main__":
    main()
