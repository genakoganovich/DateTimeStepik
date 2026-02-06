from datetime import datetime
from zoneinfo import ZoneInfo


class Event:
    UTZ_TZ = ZoneInfo("UTC")
    KEYS = ('event_time_utc', 'description')

    @staticmethod
    def create_now():
        return datetime.now(Event.UTZ_TZ)

    @staticmethod
    def create_datetime(year, month, day, hour=0, minute=0, second=0):
        return datetime(year, month, day, hour, minute, second, tzinfo=Event.UTZ_TZ)

    @staticmethod
    def create_event(values):
        return dict(zip(Event.KEYS, values))
