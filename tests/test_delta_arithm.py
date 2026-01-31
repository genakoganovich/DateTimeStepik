from src.datetime_arithm.add_days import add_days
import pytest

@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param("2025-10-20", 15, "%Y-%m-%d", "2025-11-04")
])
def test_add_days(a, b, c, expected):
    assert add_days(a, b, c) == expected



