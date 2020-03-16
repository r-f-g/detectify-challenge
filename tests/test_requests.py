from dataclasses import dataclass
from unittest.mock import patch

import numpy as np
import pytest
from requests import ConnectionError

from utils.requests import get_request_time, get_requests_times


def fake_get(url: str, **kwargs):
    @dataclass
    class FakeResponse:
        status_code: int
        text: str

    if url == "error":
        raise ConnectionError("test exception")

    return FakeResponse(status_code=200, text="OK")


@patch("requests.get", fake_get)
@pytest.mark.parametrize("url, exp_lt_time", [("error", np.nan), ("ok_url", 1),])
def test_get_request_time(url, exp_lt_time):
    """test get request time method"""
    result = np.array([get_request_time(url)], dtype=np.float)[0]
    assert result <= exp_lt_time or np.isnan(result)


@patch("requests.get", fake_get)
@pytest.mark.parametrize("url, number, exp_lt_time", [("error", 10, np.nan), ("any_other_url", 10, 1)])
def test_get_requests_times(url, number, exp_lt_time):
    """test url validation"""
    results = np.array(get_requests_times(url, number), dtype=np.float)
    assert results.size == number
    assert np.sum(results) <= number * exp_lt_time or np.isnan(results).all()
