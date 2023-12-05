import re

from aoc.utils import get_lines

matcher = re.compile(r"Card ([ 0-9]+): ([ 0-9]+) \| ([ 0-9]+)")


def solve(lines):
    winning_numbers_per_game = {}
    points_per_game = {}

    for line in lines:
        game, numbers_win, numbers_own = matcher.findall(line)[0]
        game = int(game.strip())
        numerbs_win = list(map(int, filter(None, numbers_win.split(" "))))
        numbers_own = list(map(int, filter(None, numbers_own.split(" "))))

        winning_numbers = sum(1 for n_own in numbers_own if n_own in numerbs_win)
        winning_numbers_per_game[game] = winning_numbers
        points = 2 ** (winning_numbers - 1) if winning_numbers else 0
        points_per_game[game] = points

    print(f"Total points: {sum(points_per_game.values())}")

    n_games = max(points_per_game.keys())
    number_of_cards_per_game = {}

    for i_game in range(1, n_games + 1):

        number_of_cards = number_of_cards_per_game.setdefault(i_game, 1)
        winning_numbers = winning_numbers_per_game[i_game]

        for offset in range(1, winning_numbers + 1):
            j_game = i_game + offset
            if j_game > n_games:
                break
            number_of_cards_per_game[j_game] = number_of_cards_per_game.get(j_game, 1) + number_of_cards

    print(f"Total number of cards: {sum(number_of_cards_per_game.values())}")


if __name__ == "__main__":
    lines = get_lines(4)
    # lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()
    solve(lines)
