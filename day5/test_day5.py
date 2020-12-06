from pathlib import Path

import pytest

from day5.day5 import search_num, solve_day5_part1, solve_day5_part2


@pytest.fixture
def day5_example1():
    return ["FBFBBFFRLR"]


@pytest.fixture
def day5_example2():
    return ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


@pytest.fixture
def input_day5():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return [l.strip() for l in input_file.readlines() if l]


def test_day5_part1_example(day5_example1, day5_example2):
    assert (
        solve_day5_part1(day5_example1, min_row=0, max_row=127, min_col=0, max_col=7)
        == 357
    )
    assert (
        solve_day5_part1(day5_example2, min_row=0, max_row=127, min_col=0, max_col=7)
        == 820
    )


def test_day5_part1_input(input_day5):
    assert (
        solve_day5_part1(input_day5, min_row=0, max_row=127, min_col=0, max_col=7)
        == 926
    )


def test_day5_part2_input(input_day5):
    assert (
        solve_day5_part2(input_day5, min_row=0, max_row=127, min_col=0, max_col=7)
        == 657
    )
