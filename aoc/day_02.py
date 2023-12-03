import re

import numpy as np

from aoc.utils import get_lines

game_matcher = re.compile(r"Game ([0-9]+):")
set_matcher = re.compile(r"(?:[0-9]+ (?:red|blue|green)(?:, )?)+")
color_matcher = re.compile(r"([0-9]+) (red|blue|green)")

color_codes = {"red": 0, "green": 1, "blue": 2}


def solve(lines):
    games_data = {}

    for line in lines:
        game = int(game_matcher.findall(line)[0])

        game_sets = [color_matcher.findall(match.group()) for match in set_matcher.finditer(line)]
        game_data = np.zeros((len(game_sets), 3))
        for i, game_set in enumerate(game_sets):
            for n, color in game_set:
                game_data[i, color_codes[color]] = int(n)

        games_data[game] = game_data

    games_valid = []

    for game, game_data in games_data.items():
        if not np.any(game_data > np.array([12, 13, 14])):
            games_valid.append(game)

    print(f"Sum of valid games: {sum(games_valid)}")

    games_power = []

    for game_data in games_data.values():
        game_power = np.prod(np.max(game_data, axis=0))
        games_power.append(int(game_power))

    print(f"Sum of all games power: {sum(games_power)}")


if __name__ == "__main__":
    lines = get_lines(2)
    # lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()
    solve(lines)
