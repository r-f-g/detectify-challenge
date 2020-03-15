from dataclasses import dataclass
from unittest.mock import patch

import pytest
from requests import ConnectionError

from utils.validation import get_request, validate_url


def fake_get(url: str):
    @dataclass
    class FakeResponse:
        status_code: int
        text: str

    if url == "raise":
        raise ConnectionError("page was not found")
    elif url == "error":
        return FakeResponse(status_code=500, text="server error")

    return FakeResponse(status_code=200, text="OK")


@patch("requests.get", fake_get)
@pytest.mark.parametrize("url, exp_lt_time", [("error", -1.0), ("ok_url", 1),])
def test_get_request(url, exp_lt_time):
    """test get request time method"""
    assert get_request(url) <= exp_lt_time


@patch("requests.get", fake_get)
@pytest.mark.parametrize(
    "url, number, exp_lt_time, exp_size", [("raise", 10, 0, 0), ("error", 10, -1, 10), ("any_other_url", 10, 1, 10)]
)
def test_validate_url(url, number, exp_lt_time, exp_size):
    """test url validation"""
    results = validate_url(url, number)
    assert len(results) == exp_size
    assert sum(results) <= number * exp_lt_time
