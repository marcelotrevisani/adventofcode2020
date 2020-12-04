from typing import List


def solve_day3_part1(input_list: List[str], right: int = 3, down: int = 1) -> int:
    h_pos = right
    v_pos = down
    num_tree = 0
    while v_pos < len(input_list):
        line = input_list[v_pos].strip()
        if line[h_pos % len(line)] == "#":
            num_tree += 1
        v_pos += down
        h_pos += right
    return num_tree
