import logging
import time
from typing import Any, Dict, List, Optional

import requests
from requests import ConnectionError
from tqdm import tqdm

logger = logging.getLogger(__name__)


def get_request_time(url: str, params: Optional[Dict[str, Any]] = None) -> Optional[float]:
    """timeit GET request"""
    try:
        start = time.monotonic()
        requests.get(url, params=params)
        return time.monotonic() - start
    except ConnectionError as error:
        logger.exception(error)
        return None


def get_requests_times(url: str, number: int, params: Optional[Dict[str, Any]] = None) -> List[Optional[float]]:
    """timeit number of GET requests"""
    start = time.monotonic()
    logger.info(f"start test of url {url} with params {params}")
    results = [get_request_time(url, params=params) for _ in tqdm(range(number), desc=url, leave=False)]
    logger.info(f"finished test of {url} at time {time.monotonic() - start:.3f}")
    return results
