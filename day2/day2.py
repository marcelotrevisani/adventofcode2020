import re
from typing import List


def solve_day2_part1(list_input: List[str]) -> int:
    re_info = re.compile(r"\s*(\d+)-(\d+)\s+(\w+):\s+(\w+)")
    valid_passwd = 0
    for line in list_input:
        min_rep, max_rep, letter, word = re_info.match(line).groups()
        count_letter = word.count(letter)
        if int(max_rep) >= count_letter >= int(min_rep):
            valid_passwd += 1
    return valid_passwd
