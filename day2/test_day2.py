from pathlib import Path

import pytest

from day2.day2 import solve_day2_part1


@pytest.fixture(scope="session")
def input_day2():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return [line.strip() for line in input_file.readlines() if line.strip()]


@pytest.fixture(scope="session")
def input_example_day2():
    return ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_day2_part1_example(input_example_day2):
    assert solve_day2_part1(input_example_day2) == 2
    assert solve_day2_part1(["1-2 a: aaabc"]) == 0


def test_day2_part1_input(input_day2):
    assert solve_day2_part1(input_day2) == 620
