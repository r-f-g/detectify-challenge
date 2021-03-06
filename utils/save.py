import logging
import os
from typing import Any, Dict, Iterable, List

logger = logging.getLogger(__name__)


def create_line(array: Iterable, sep: str) -> str:
    """create row of results file"""
    safe_array = [str(item) if item is not None else "" for item in array]
    return f"{sep.join(safe_array)}{os.linesep}"


def get_from_list(array: List, index: int) -> Any:
    """try get from array"""
    try:
        return array[index]
    except IndexError:
        return None


def save_results(file_name: str, test_results: Dict[str, List[float]], sep: str = ";", mode: str = "w") -> None:
    """save test results to file"""
    n_rows = max([len(results) for results in test_results.values()])
    logger.info(f"number of results {n_rows}")

    with open(file_name, mode=mode) as file:
        file.write(create_line(test_results.keys(), sep))

        for i in range(n_rows):
            results = [get_from_list(test_results[key], i) for key in test_results]
            file.write(create_line(results, sep))
