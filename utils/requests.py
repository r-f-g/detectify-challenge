import logging
import time
from typing import List

import requests
from requests import ConnectionError
from tqdm import tqdm

logger = logging.getLogger(__name__)


def get_request_time(url: str) -> float:
    """timeit GET request"""
    start = time.monotonic()
    response = requests.get(url)

    if 200 <= response.status_code < 300:
        return time.monotonic() - start
    else:
        logger.error(f"response return code {response.status_code} with text {response.text}")
        return -1.0


def get_requests_times(url: str, number: int) -> List[float]:
    """validate url"""
    results = []
    start = time.monotonic()

    logger.info(f"start test of url {url}")
    try:
        results = [get_request_time(url) for _ in tqdm(range(number), desc="validation", leave=False)]
        logger.info(f"finished test of {url} at time {time.monotonic() - start:.3f}")
    except ConnectionError as error:
        logger.exception(error)
        logger.error(f"the page {url} is inaccessible")

    return results
