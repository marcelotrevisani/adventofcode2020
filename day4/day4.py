import os
import re


def solve_day4_part1(raw_input: str) -> int:
    raw_list_passports = raw_input.split(os.linesep * 2)
    re_passport_fields = re.compile(r"(\w+):([#]*\w+)")
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    num_valid_passports = 0
    for passport in raw_list_passports:
        passport = dict(re_passport_fields.findall(passport))
        if set(required_fields).issubset(passport.keys()):
            num_valid_passports += 1
    return num_valid_passports
