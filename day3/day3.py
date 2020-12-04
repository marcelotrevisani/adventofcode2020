from typing import List, Tuple


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


def solve_day3_part2(list_slopes: List[Tuple[int, int]], input_list: List[str]) -> int:
    result = solve_day3_part1(
        input_list, right=list_slopes[0][0], down=list_slopes[0][1]
    )
    for right, down in list_slopes[1:]:
        result *= solve_day3_part1(input_list, right=right, down=down)
    return result
