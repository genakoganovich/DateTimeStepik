from src.datetime_object.create_date import create_date
from src.datetime_object.combine_datetime import combine_datetime
from src.datetime_object.set_alarm_clock import set_alarm_clock
from src.datetime_object.get_datetime_attr import get_datetime_attr

def test_create_date():
    assert str(create_date(2023, 10, 5)) == "2023-10-05"


def test_combine_datetime():
    assert str(combine_datetime(2025, 9, 25, 18, 0)) == "2025-09-25 18:00:00"

def test_set_alarm_clock():
    assert str(set_alarm_clock(7, 30, 0)) == "07:30:00"

def test_get_datetime_attr():
    assert (get_datetime_attr(2025, 10, 2, 14, 30, 5)==
            "Дата: 2025-10-02\nВремя: 14:30:05")