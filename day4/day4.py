import os
import re
from typing import Dict

REQUIRED_FILES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate_byr(val: str) -> bool:
    return len(val) == 4 and int(val) >= 1920 and int(val) <= 2002


def validate_iyr(val: str) -> bool:
    return len(val) == 4 and int(val) >= 2010 and int(val) <= 2020


def validate_eyr(val: str) -> bool:
    return len(val) == 4 and int(val) >= 2020 and int(val) <= 2030


def validate_hgt(val: str) -> bool:
    try:
        height, unit = re.fullmatch(r"(\d+)(cm|in)", val).groups()
    except AttributeError:
        return False
    height = int(height)
    if unit == "cm":
        return 150 <= height <= 193
    if unit == "in":
        return 59 <= height <= 76
    return False


def validate_hcl(val: str) -> bool:
    return re.fullmatch(r"#[0-9a-f]{6}", val) is not None


def validate_ecl(val: str) -> bool:
    return val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_pid(val: str) -> bool:
    return re.fullmatch(r"\d{9}", val) is not None


def is_valid(passport: Dict, strict_validation: bool = False) -> bool:
    if strict_validation is False:
        return REQUIRED_FILES.issubset(passport.keys())

    validation = {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid,
    }

    for field, check in validation.items():
        if check(passport.get(field, "")) is False:
            return False
    return True


def solve_day4_part1(raw_input: str, strict_validation: bool = False) -> int:
    raw_list_passports = raw_input.split(os.linesep * 2)
    re_passport_fields = re.compile(r"(\w+):([#]*\w+)")
    num_valid_passports = 0
    for passport in raw_list_passports:
        passport = dict(re_passport_fields.findall(passport))
        if is_valid(passport, strict_validation):
            num_valid_passports += 1
    return num_valid_passports


def solve_day4_part2(raw_input: str) -> int:
    return solve_day4_part1(raw_input, strict_validation=True)
