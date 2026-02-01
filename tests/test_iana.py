import pytest
from src.datetime_iana.create_aware import create_aware


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
