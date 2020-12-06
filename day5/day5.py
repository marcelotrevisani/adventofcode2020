import bisect
from enum import Enum, auto
from typing import List


class SeatPosition(Enum):
    UPPER = auto()
    LOWER = auto()


def solve_day5_part1(
    input_list: List[str],
    *,
    min_row: int = 0,
    max_row: int = 127,
    min_col: int = 0,
    max_col: int = 7,
) -> int:
    max_id = 0
    for line in input_list:
        line = line.strip()
        row = [SeatPosition.UPPER if n == "B" else SeatPosition.LOWER for n in line[:7]]
        col = [SeatPosition.UPPER if n == "R" else SeatPosition.LOWER for n in line[7:]]
        max_id = max(
            max_id,
            search_num(min_row, max_row, row) * 8 + search_num(min_col, max_col, col),
        )
    return max_id


def search_num(lower_seat: int, upper_seat: int, seq: List[SeatPosition]) -> int:
    if len(seq) == 1:
        return lower_seat if seq[0] == SeatPosition.LOWER else upper_seat
    if seq[0] == SeatPosition.UPPER:
        return search_num(
            lower_seat + ((upper_seat - lower_seat + 1) // 2), upper_seat, seq[1:]
        )
    elif seq[0] == SeatPosition.LOWER:
        return search_num(
            lower_seat, lower_seat + ((upper_seat - lower_seat) // 2), seq[1:]
        )


def solve_day5_part2(
    input_list: List[str],
    *,
    min_row: int = 0,
    max_row: int = 127,
    min_col: int = 0,
    max_col: int = 7,
) -> int:
    sorted_ids = []
    for line in input_list:
        line = line.strip()
        row = [SeatPosition.UPPER if n == "B" else SeatPosition.LOWER for n in line[:7]]
        col = [SeatPosition.UPPER if n == "R" else SeatPosition.LOWER for n in line[7:]]
        bisect.insort(
            sorted_ids,
            search_num(min_row, max_row, row) * 8 + search_num(min_col, max_col, col),
        )
    return search_missing_id(sorted_ids)


def search_missing_id(sorted_ids: List[int]) -> int:
    for _id, num in enumerate(sorted_ids[1:], start=1):
        if sorted_ids[_id - 1] + 1 != num:
            return sorted_ids[_id - 1] + 1
