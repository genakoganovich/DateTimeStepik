import calendar

class EventStorage:
    def __init__(self):
        self.events = {}  # (year, month, day) -> list[str]



class CalendarApp:
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
        date = input("Дата (YYYY-MM-DD): ")
        title = input("Название: ")

        self.storage.add_event(date, title)
        print("Событие добавлено")

    def cmd_view(self, parts):
        if len(parts) != 4:
            print("Использование: view <год> <месяц> <день>")
            return

        year, month, day = map(int, parts[1:])
        events = self.storage.get_events(year, month, day)

        if not events:
            print("Событий нет")
        else:
            for e in events:
                print("-", e)


def main():
    calendar_app = CalendarApp()
    calendar_app.run()


if __name__ == "__main__":
    main()
