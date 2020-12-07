import os
import re


def solve_day6_part1(raw_input: str):
    groups_list = raw_input.split(os.linesep * 2)
    re_answers = re.compile(r"([a-z])", re.MULTILINE)
    sum_answers = 0
    for group in groups_list:
        sum_answers += len(set(re_answers.findall(group)))
    return sum_answers
