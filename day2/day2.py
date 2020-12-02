import re
from typing import List


def solve_day2_part1(list_input: List[str]) -> int:
    re_info = re.compile(r"\s*(\d+)-(\d+)\s+(\w+):\s+(\w+)")
    num_valid_passwd = 0
    for line in list_input:
        min_rep, max_rep, letter, word = re_info.match(line).groups()
        count_letter = word.count(letter)
        if int(max_rep) >= count_letter >= int(min_rep):
            num_valid_passwd += 1
    return num_valid_passwd


def solve_day2_part2(list_input: List[str]) -> int:
    re_info = re.compile(r"\s*(\d+)-(\d+)\s+(\w+):\s+(\w+)")
    num_valid_passwd = 0
    for line in list_input:
        pos1, pos2, letter, word = re_info.match(line).groups()
        if (word[int(pos1) - 1] == letter) ^ (word[int(pos2) - 1] == letter):
            num_valid_passwd += 1
    return num_valid_passwd
