from pathlib import Path

import pytest

from day4.day4 import solve_day4_part1


@pytest.fixture
def example_day4():
    return """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


@pytest.fixture
def input_day4():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        return input_file.read()


def test_day4_part1_example(example_day4):
    assert solve_day4_part1(example_day4) == 2


def test_day4_part1_input(input_day4):
    assert solve_day4_part1(input_day4) == 196
