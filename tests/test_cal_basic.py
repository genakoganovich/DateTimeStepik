import pytest
from src.cal_basic.get_leap import get_leap
from src.cal_basic.get_leap_range import get_leap_range

@pytest.mark.parametrize("a, expected", [
    pytest.param(2024, "LEAP")
])
def test_get_leap(a,expected):
    assert get_leap(a) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param(2020, 2030, "\n".join(map(str, [2020, 2024, 2028]))),
])
def test_get_leap_range(a, b, expected):
    assert get_leap_range(a, b) == expected