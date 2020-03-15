import os
from typing import Any, Iterable

import pytest

from utils.save import create_line, get_from_list, save_results


@pytest.mark.parametrize(
    "array, exp_line", [({"a": [], "b": []}.keys(), f"a;b{os.linesep}"), ([1, 2, 3], f"1;2;3{os.linesep}")]
)
def test_create_line(array: Iterable, exp_line: str):
    """test function to create line of results file"""
    assert create_line(array, ";") == exp_line, "lines are different"


@pytest.mark.parametrize(
    "array, index, exp_value", [([1, 2, 3], 0, 1), (["1", "2"], 1, "2"), ([1], 1, None), ([], 10, None),]
)
def test_get_from_list(array: list, index: int, exp_value: Any):
    """test get value from list by index"""
    assert get_from_list(array, index) == exp_value, "get value was not expected"


def test_save_results(tmpdir):
    """test save results to csv file"""
    results = {"a": [1, 2, 3], "b": [], "c": [1]}
    save_results(tmpdir.join("test.csv"), results)

    with open(tmpdir.join("test.csv"), mode="r") as file:
        csv_file = file.readlines()

    assert len(csv_file) == 4, "file has wrong number of rows"
    assert csv_file[0] == f"a;b;c{os.linesep}"
    assert csv_file[1] == f"1;;1{os.linesep}"
    assert csv_file[2] == f"2;;{os.linesep}"
    assert csv_file[3] == f"3;;{os.linesep}"
