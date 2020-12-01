from pathlib import Path

from day1.day1 import solution_day1


def test_day1_example():
    assert solution_day1([1721, 979, 366, 299, 675, 1456]) == 514579


def test_day1_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as input_file:
        all_numbers = [int(line) for line in input_file.readlines() if line.strip()]
        assert solution_day1(all_numbers) == 1013211
