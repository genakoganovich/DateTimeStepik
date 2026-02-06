from collections import defaultdict


class EventStorage:
    def __init__(self):
        self.events = defaultdict(list)

    def add_event(self, event_date, event):
        self.events[event_date].append(event)

    def get_events(self, event_date):
        return self.events.get(event_date, [])

    def get_days(self, year, month):
        return [
            d.day
            for d in self.events
            if d.year == year and d.month == month
        ]