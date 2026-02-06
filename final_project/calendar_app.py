import calendar
from datetime import date

from final_project.event import Event
from final_project.event_storage import EventStorage
from final_project.red_text_calendar import RedTextCalendar


class CalendarApp:
    COMMANDS = (
        "show <год> <месяц>",
        "add",
        "view <год> <месяц> <день>",
        "help",
        "exit",
    )


    def __init__(self):
        self.storage = EventStorage()
        self.red_text_calendar = RedTextCalendar()

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
        event_date = date(*nums)
        hour, minute = map(int, input("Время (HH:MM): ").split(':'))
        event_datetime = Event.create_datetime(*nums, hour, minute)
        description = input("Название: ")
        event = Event.create_event((event_datetime, description))
        self.storage.add_event(event_date, event)
        print("Событие добавлено")

    def cmd_view(self, parts):
        if len(parts) != 4:
            print("Использование: view <год> <месяц> <день>")
            return

        nums = map(int, parts[1:])
        event_date = date(*nums)
        events = self.storage.get_events(event_date)

        if not events:
            print("Событий нет")
        else:
            for e in events:
                print("-", e)

    def cmd_help(self):
        print(self.COMMANDS)

    def cmd_unknown(self):
        print("Неизвестная команда")
        self.cmd_help()

    def show_current_month(self):
        now = Event.create_now()
        self.show_month(now.year, now.month)

    def show_month(self, year, month):
        self.red_text_calendar.set_red_days(self.storage.get_days(year, month))
        print(self.red_text_calendar.formatmonth(year, month))
        self.red_text_calendar.reset_red_days()