from pathlib import Path

import pytest

from day3.day3 import solve_day3_part1, solve_day3_part2


@pytest.fixture
def example_day3():
    return """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split(
        "\n"
    )


@pytest.fixture
def input_day3():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return [l.strip() for l in input_file.readlines() if l.strip()]


def test_day3_part1_example(example_day3):
    assert solve_day3_part1(example_day3) == 7
    assert solve_day3_part1(example_day3, right=1, down=1) == 2
    assert solve_day3_part1(example_day3, right=3, down=1) == 7
    assert solve_day3_part1(example_day3, right=5, down=1) == 3
    assert solve_day3_part1(example_day3, right=7, down=1) == 4
    assert solve_day3_part1(example_day3, right=1, down=2) == 2


def test_day3_part1_input(input_day3):
    assert solve_day3_part1(input_day3) == 262


def test_day3_part2_example(example_day3):
    assert (
        solve_day3_part2([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], example_day3) == 336
    )


def test_day3_part2_input(input_day3):
    assert (
        solve_day3_part2([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], input_day3)
        == 2698900776
    )
