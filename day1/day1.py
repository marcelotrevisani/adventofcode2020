from typing import List


def get_min_start(sorted_list: List[int]) -> int:
    for pos, num in enumerate(sorted_list):
        if num < 2020 // 2:
            return pos
    return len(sorted_list) - 1


def solution_day1(input_list: List[int]) -> int:
    input_list.sort(reverse=True)
    start_min_seq = get_min_start(input_list)
    ptr = len(input_list) - 1

    for num in input_list[:start_min_seq]:
        while ptr >= start_min_seq:
            if num + input_list[ptr] == 2020:
                return num * input_list[ptr]
            if num + input_list[ptr] > 2020:
                break
            ptr -= 1
        ptr = max(ptr, start_min_seq)
    raise Exception("It was not possible to find the numbers which the sum is 2020")
