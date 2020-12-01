from typing import List


def get_min_start(sorted_list: List[int], stop_num: int = 2020) -> int:
    for pos, num in enumerate(sorted_list):
        if num < stop_num // 2:
            return pos
    raise ValueError("It was not possible to find the numbers which the sum is 2020")


def solution_day1_part1(
    input_list: List[int], *, stop_num: int = 2020, is_sorted: bool = False
) -> int:
    if not is_sorted:
        input_list.sort(reverse=True)
    start_min_seq = get_min_start(input_list, stop_num)
    ptr = len(input_list) - 1

    for num in input_list[:start_min_seq]:
        while ptr >= start_min_seq:
            if num + input_list[ptr] == stop_num:
                return num * input_list[ptr]
            if num + input_list[ptr] > stop_num:
                break
            ptr -= 1
        ptr = max(ptr, start_min_seq)
    raise ValueError("It was not possible to find the numbers which the sum is 2020")


def solution_day1_part2(input_list: List[int]) -> int:
    input_list.sort(reverse=True)
    for pos, num in enumerate(input_list):
        try:
            return num * solution_day1_part1(
                input_list[pos:], stop_num=2020 - num, is_sorted=True
            )
        except ValueError:
            continue
