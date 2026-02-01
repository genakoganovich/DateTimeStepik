import pytest
from src.datetime_tzinfo.check_naive import check_naive
from src.datetime_tzinfo.create_utc import create_dt_utc
from src.datetime_tzinfo.create_dt_utc_delta import create_dt_utc_delta
from src.datetime_tzinfo.create_dt_utc_delta_min import create_dt_utc_delta_min
from src.datetime_tzinfo.get_utc_details import get_utc_details


@pytest.mark.parametrize("dt_string, expected", [
    pytest.param("2025 10 20", "Naive", id="naive"),
])
def test_check_naive(dt_string, expected):
    assert check_naive(dt_string) == expected

@pytest.mark.parametrize("a, b, c, d, e, expected", [
    pytest.param(2025, 9, 25, 15, 30, "2025-09-25 15:30:00+00:00", id="UTC"),
])
def test_create_dt_utc(a, b, c, d, e, expected):
    assert str(create_dt_utc(a, b, c, d, e)) == expected

@pytest.mark.parametrize("a, b, c, d, e, f, expected", [
    pytest.param(2025, 10, 20, 18, 0, 5, "2025-10-20 18:00:00+05:00", id="offset 5"),
])
def test_create_dt_utc_delta(a, b, c, d, e, f, expected):
    assert str(create_dt_utc_delta(a, b, c, d, e, f)) == expected

@pytest.mark.parametrize("a, b, c, d, e, f, expected", [
    pytest.param(2025, 9, 25, 18, 0, 180, "2025-09-25 18:00 [UTC+03:00]", id="offset 180"),
])
def test_create_dt_utc_delta_min(a, b, c, d, e, f, expected):
    assert str(create_dt_utc_delta_min(a, b, c, d, e, f)) == expected

@pytest.mark.parametrize("a, expected", [
    pytest.param("2025-10-20T10:00:00-04:00", "10:00:00\n-1 day, 20:00:00", id="ISO 8601"),
])
def test_get_utc_details(a, expected):
    assert str(get_utc_details(a)) == expected