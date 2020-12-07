from pathlib import Path

import pytest

from day7.day7 import solve_day7_part1


@pytest.fixture
def input_day7() -> str:
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return input_file.read()


@pytest.fixture
def example_day7() -> str:
    return """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def test_day7_part1_example(example_day7):
    assert solve_day7_part1(example_day7) == 4


def test_day7_part1_input(input_day7):
    assert solve_day7_part1(input_day7) == 226
