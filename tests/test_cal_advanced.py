import pytest
from src.cal_advanced.count_full_weeks import count_full_weeks
from src.cal_advanced.is_friday_13 import is_friday_13
from src.cal_advanced.get_last_tuesday import get_last_tuesday
from src.cal_advanced.get_total_work_days import get_total_work_days


@pytest.mark.parametrize("a, expected", [
    pytest.param([2025, 9], 4)
])
def test_count_full_weeks(a,expected):
    assert count_full_weeks(a) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param([2026, 6], 13, False),
])
def test_is_friday_13(a, b, expected):
    assert is_friday_13(a, b) == expected

@pytest.mark.parametrize("a, expected", [
    pytest.param([2025, 9], 30),
])
def test_get_last_tuesday(a,expected):
    assert get_last_tuesday(a) == expected

@pytest.mark.parametrize("a, expected", [
    pytest.param([2025, 9], 22),
])
def test_get_total_work_days(a,expected):
    assert get_total_work_days(a) == expected