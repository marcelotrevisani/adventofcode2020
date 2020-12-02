from pathlib import Path

import pytest

from day1.day1 import solve_day1_part1, solve_day1_part2


@pytest.fixture(scope="function")
def input_example():
    return [1721, 979, 366, 299, 675, 1456]


@pytest.fixture(scope="function")
def list_input_file():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return [int(line) for line in input_file.readlines() if line.strip()]


def test_day1_part1_example(input_example):
    assert solve_day1_part1(input_example) == 514579


def test_day1_input_part1(list_input_file):
    assert solve_day1_part1(list_input_file) == 1013211


def test_day1_part2_example(input_example):
    assert solve_day1_part2(input_example) == 241861950


def test_day1_input_part2(list_input_file):
    assert solve_day1_part2(list_input_file) == 13891280
