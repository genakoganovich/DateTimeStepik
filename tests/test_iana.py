import pytest
from src.datetime_iana.create_aware import create_aware
from src.datetime_iana.save_db_utc import save_db_utc
from src.datetime_iana.get_offset import get_offset
from src.datetime_iana.make_aware import make_aware


@pytest.mark.parametrize(
    "nums, src_tz, target, expected",
    [
        (
            [2025, 11, 5, 9, 0],
            "America/Los_Angeles",
            [
                ("Лондон", "Europe/London"),
                ("Москва", "Europe/Moscow"),
                ("Токио", "Asia/Tokyo"),
            ],
            "\n".join([
                "Лондон: 2025-11-05 17:00:00",
                "Москва: 2025-11-05 20:00:00",
                "Токио: 2025-11-06 02:00:00",
            ]),
        ),
    ],
)
def test_create_aware(nums, src_tz, target, expected):
    assert create_aware(nums, src_tz, target) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param([2025, 10, 20, 10, 0, 0], "Australia/Sydney", "2025-10-19 23:00:00")
])
def test_save_db_utc(a, b, expected):
    assert save_db_utc(a, b) == expected

@pytest.mark.parametrize("a, expected", [
    pytest.param("Europe/Berlin", f"{'1:00:00'}\n{'2:00:00'}")
])
def test_get_offset(a, expected):
    assert get_offset(a) == expected

@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param([2025, 9, 25, 18, 30], "Europe/Moscow", "America/New_York", "2025-09-25 11:30:00-04:00")
])
def test_make_aware(a, b, c, expected):
    assert str(make_aware(a, b, c)) == expected