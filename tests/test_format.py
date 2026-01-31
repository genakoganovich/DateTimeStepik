from src.strf_strp.format_date import format_date
from src.strf_strp.get_month import get_month
from src.strf_strp.create_logfile_name import create_logfile_name
from src.strf_strp.parse_short_month import parse_short_month
from src.strf_strp.reformat_date import reformat_date
import pytest


@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param(2025, 9, 25, "25.09.2025", id="2025"),
])
def test_format_date(a, b, c, expected):
    assert format_date(a, b, c) == expected


@pytest.mark.parametrize("a, expected", [
    pytest.param("2025-09-25", "September", id="September"),
])
def test_get_month(a, expected):
    assert get_month(a) == expected


@pytest.mark.parametrize("a, b, expected", [
    pytest.param("2025 9 25 18 5 3", "%Y %m %d %H %M %S", "2025-09-25_18-05-03"),
])
def test_create_logfile_name(a, b, expected):
    assert create_logfile_name(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    pytest.param("25-Sep-2025 15:30:05", "%d-%b-%Y %H:%M:%S", 15)
])
def test_parse_short_month(a, b, expected):
    assert parse_short_month(a, b) == expected


@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param("09/25/2025", "%m/%d/%Y", "%Y-%m-%d", "2025-09-25"),
])
def test_reformat_date(a, b, c, expected):
    assert reformat_date(a, b, c) == expected
