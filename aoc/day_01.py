from aoc.utils import get_lines


def replace_spelled_digits(line: str) -> str:
    return (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )


def solve(lines):
    nums = []
    for line in lines:
        num_in_line = list(filter(lambda c: c.isdigit(), line))
        num = int(f"{num_in_line[0]}{num_in_line[-1]}")
        nums.append(num)

    print(f"Sum of 2-digit numbers: {sum(nums)}")


def solve2(lines):
    nums = []
    for line in lines:
        line = replace_spelled_digits(line)
        num_in_line = list(filter(lambda c: c.isdigit(), line))
        num = int(f"{num_in_line[0]}{num_in_line[-1]}")
        nums.append(num)

    print(f"Sum of 2-digit numbers (with spelled digits): {sum(nums)}")


if __name__ == "__main__":
    lines = get_lines(1)
    # lines = """1abc2
    # pqr3stu8vwx
    # a1b2c3d4e5f
    # treb7uchet""".splitlines()
    solve(lines)
    # lines = """two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen""".splitlines()
    solve2(lines)
