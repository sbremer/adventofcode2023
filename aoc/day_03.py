import re
from collections import defaultdict

import numpy as np

from aoc.utils import get_lines


def solve(lines):
    data_chars = np.array([list(line) for line in lines])

    is_symbol = np.vectorize(lambda c: not c.isdigit() and c != ".")
    is_gear_symbol = np.vectorize(lambda c: c == "*")

    data_is_symbol = is_symbol(data_chars)
    data_is_gear_symbol = is_gear_symbol(data_chars)

    data_shape = data_is_symbol.shape

    match_numbers = re.compile(r"[0-9]+")

    numbers_by_gear_pos = defaultdict(list)

    valid_part_numbers = []

    for i, line in enumerate(lines):
        for match in match_numbers.finditer(line):

            surrounding_pos = max(0, i - 1), max(0, match.start() - 1)
            surrounding = slice(max(0, i - 1), min(data_shape[0], i + 2)), slice(
                max(0, match.start() - 1), min(data_shape[1], match.end() + 1)
            )

            num = int(match.group())

            symbol_in_surrounding = np.any(data_is_symbol[surrounding])
            if symbol_in_surrounding:
                valid_part_numbers.append(num)

            gear_symbols_in_surrounding = data_is_gear_symbol[surrounding]
            if np.sum(gear_symbols_in_surrounding) == 1:
                gear_pos_array = np.argwhere(gear_symbols_in_surrounding)
                gear_pos = gear_pos_array[0, 0] + surrounding_pos[0], gear_pos_array[0, 1] + surrounding_pos[1]
                numbers_by_gear_pos[gear_pos].append(num)

    print(f"Sum of all valid part numbers: {sum(valid_part_numbers)}")

    gear_ratios = []
    for gear_numbers in numbers_by_gear_pos.values():
        if len(gear_numbers) == 2:
            gear_ratios.append(np.prod(gear_numbers))

    print(f"Sum of all gear ratios: {sum(gear_ratios)}")


if __name__ == "__main__":
    lines = get_lines(3)
    #     lines = """467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598..
    # ..........""".splitlines()
    solve(lines)
