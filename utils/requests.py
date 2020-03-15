import logging
import time
from typing import Any, Dict, List, Optional

import requests
from tqdm import tqdm

logger = logging.getLogger(__name__)


def get_request_time(url: str, params: Optional[Dict[str, Any]] = None) -> Optional[float]:
    """timeit GET request"""
    start = time.monotonic()
    response = requests.get(url, params=params)

    if 200 <= response.status_code < 300:
        return time.monotonic() - start
    else:
        logger.error(f"response return code {response.status_code} with text {response.text}")
        return None


def get_requests_times(url: str, number: int, params: Optional[Dict[str, Any]] = None) -> List[Optional[float]]:
    """timeit number of GET requests"""
    start = time.monotonic()
    logger.info(f"start test of url {url} with params {params}")
    results = [get_request_time(url, params=params) for _ in tqdm(range(number), desc=url, leave=False)]
    logger.info(f"finished test of {url} at time {time.monotonic() - start:.3f}")
    return results
