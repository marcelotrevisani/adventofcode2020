from pathlib import Path

import pytest

from day6.day6 import solve_day6_part1, solve_day6_part2


@pytest.fixture
def input_day6() -> str:
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return input_file.read()


@pytest.fixture
def example_day6() -> str:
    return """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_day6_part1_example(example_day6):
    assert solve_day6_part1(example_day6) == 11


def test_day6_part1_input(input_day6):
    assert solve_day6_part1(input_day6) == 6585


def test_day6_part2_example(example_day6):
    assert solve_day6_part2(example_day6) == 6


def test_day6_part2_input(input_day6):
    assert solve_day6_part2(input_day6) == 3276
