import re
from typing import Dict, Set


def solve_day7_part1(raw_input: str) -> int:
    re_inside_bags = re.compile(r"\d+\s+(\w+\s+\w+)\s+bag[s]*[\.,]")
    all_bags = {}
    key_shiny_gold = {"shiny gold"}
    for line in re.finditer(
        r"(\w+\s+\w+)\s+bags\s+contain\s+(.*)", raw_input, re.MULTILINE
    ):
        main_bag, inside_bags = line.groups()
        all_bags[main_bag] = set(re_inside_bags.findall(inside_bags))
        if key_shiny_gold.intersection(all_bags[main_bag]):
            key_shiny_gold.add(main_bag)

    num_shiny_gold_bags = 0
    for bag, sub_bags in all_bags.items():
        if does_bag_contain_shiny_gold(sub_bags, all_bags, key_shiny_gold):
            num_shiny_gold_bags += 1
    return num_shiny_gold_bags


def does_bag_contain_shiny_gold(
    bags_set: Set[str], all_bags: Dict, keys_shiny_gold: Set[str]
) -> bool:
    if bags_set.intersection(keys_shiny_gold):
        return True
    for bag in bags_set:
        if all_bags.get(bag, None) is None:
            continue
        if does_bag_contain_shiny_gold(all_bags[bag], all_bags, keys_shiny_gold):
            keys_shiny_gold.add(bag)
            return True
    return False


def solve_day7_part2(raw_input: str) -> int:
    re_inside_bags = re.compile(r"(\d+)\s+(\w+\s+\w+)\s+bag[s]*[\.,]")
    all_bags = {}
    for line in re.finditer(
        r"(\w+\s+\w+)\s+bags\s+contain\s+(.*)", raw_input, re.MULTILINE
    ):
        main_bag, inside_bags = line.groups()
        all_bags[main_bag] = re_inside_bags.findall(inside_bags)
    return get_num_bags("shiny gold", all_bags)


def get_num_bags(bag_name: str, all_bags: Dict) -> int:
    num_bags = 0
    for quant, name in all_bags[bag_name]:
        quant = int(quant)
        num_bags += quant
        if all_bags.get(name, None):
            num_bags += quant * get_num_bags(name, all_bags)
    return num_bags
