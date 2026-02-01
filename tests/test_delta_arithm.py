import pytest
from src.datetime_arithm.add_days import add_days
from src.datetime_arithm.get_rocket_signal_dt import get_rocket_signal_dt
from src.datetime_arithm.get_new_year_delta import get_new_year_delta
from src.datetime_arithm.get_duration import get_duration
from src.datetime_arithm.get_total_duration import get_total_duration



@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param("2025-10-20", 15, "%Y-%m-%d", "2025-11-04")
])
def test_add_days(a, b, c, expected):
    assert add_days(a, b, c) == expected

@pytest.mark.parametrize("a, b, c, d, e, expected", [
    pytest.param("2025-09-25 18:00:00", 3, 30, 0, "%Y-%m-%d %H:%M:%S", "2025-09-25 14:30:00")
])
def test_get_rocket_signal_dt(a, b, c, d, e, expected):
    assert get_rocket_signal_dt(a, b, c, d, e) == expected

@pytest.mark.parametrize("a, expected", [
    pytest.param("2025-12-25", 7),
])
def test_get_new_year_delta(a, expected):
    assert get_new_year_delta(a) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param("10:00:00", "11:30:00", 90)
])
def test_get_duration(a, b, expected):
    assert get_duration(a, b) == expected


@pytest.fixture
def durations():
    days = [1, 2]
    hours = [10, 5]
    minutes = [30, 45]
    return [dict(zip(['days', 'hours', 'minutes'], t)) for t in zip(days, hours, minutes)]

def test_get_total_duration(durations):
    expected = "3 58500"
    assert get_total_duration(durations) == expected