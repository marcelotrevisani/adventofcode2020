from pathlib import Path

import pytest

from day4.day4 import (
    solve_day4_part1,
    solve_day4_part2,
    validate_byr,
    validate_ecl,
    validate_eyr,
    validate_hcl,
    validate_hgt,
    validate_iyr,
    validate_pid,
)


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


def test_day4_part2_invalid():
    invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
    assert solve_day4_part2(invalid) == 0


def test_day4_part2_valid():
    valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
    assert solve_day4_part2(valid) == 4


def test_validate_byr():
    assert validate_byr("2000")
    assert not validate_byr("89")
    assert not validate_byr("1000")
    assert not validate_byr("1919")
    assert not validate_byr("2003")


def test_validate_iyr():
    assert validate_iyr("2011")
    assert not validate_iyr("89")
    assert not validate_iyr("1000")
    assert not validate_iyr("2009")
    assert not validate_iyr("2021")


def test_validate_eyr():
    assert validate_eyr("2025")
    assert not validate_eyr("89")
    assert not validate_eyr("2019")
    assert not validate_eyr("2031")


def test_validate_hgt():
    assert validate_hgt("155cm")
    assert validate_hgt("150cm")
    assert validate_hgt("193cm")
    assert validate_hgt("59in")
    assert validate_hgt("76in")
    assert validate_hgt("70in")

    assert not validate_hgt("149cm")
    assert not validate_hgt("194cm")
    assert not validate_hgt("77in")
    assert not validate_hgt("58in")

    assert not validate_hgt("155mc")
    assert not validate_hgt("a155")


def test_validate_hcl():
    assert validate_hcl("#123abc")
    assert not validate_hcl("#123abz")
    assert not validate_hcl("123abc")


def test_validate_ecl():
    assert validate_ecl("brn")
    assert not validate_ecl("wat")


def test_validate_pid():
    assert validate_pid("000000001")
    assert not validate_pid("0123456789")


def test_day4_part2_input(input_day4):
    assert solve_day4_part2(input_day4) == 114
