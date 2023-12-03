from functools import reduce

import regex as re

colour_count_limits = {"red": 12, "green": 13, "blue": 14}


def extract_lines(input: str) -> list[str]:
    split = input.split("\n")
    return split


def extract_colour_counts(line: str) -> list[tuple[str, ...]]:
    """From a single line, get the count of each colour occurrence."""
    target_colours_re: str = "|".join([key for key in colour_count_limits.keys()])
    line_colours_re_pattern = f"(([0-9]+) ({target_colours_re}))(?:[;, \n]|$)"
    line_colour_counts = re.findall(line_colours_re_pattern, line)
    return line_colour_counts


def convert_re_matches_to_max_occurrence(
    re_matches: list[tuple[str, ...]]
) -> dict[str, int]:
    """Create a dict of max occurrences of colours."""
    max_colour_counts: dict[str, int] = {}
    for re_match in re_matches:
        colour_name = re_match[2]
        colour_count = int(re_match[1])
        if colour_name in max_colour_counts:
            if colour_count > max_colour_counts[colour_name]:
                max_colour_counts[colour_name] = colour_count
        else:
            max_colour_counts[colour_name] = colour_count
    return max_colour_counts


def max_colours_exceeded(line_colour_count_maxes: dict[str, int]) -> bool:
    """Verify if the available number of colour counts have been exceeded."""
    for colour, count in line_colour_count_maxes.items():
        if count > colour_count_limits[colour]:
            return True
    return False


def calculate_possible_games_ids_sum(game_records_doc: str) -> int:
    """Sum all valid games, those that have sufficient cube colours."""
    input_lines = extract_lines(game_records_doc)

    potential_games = []
    for index, line in enumerate(input_lines):
        re_matches = extract_colour_counts(line)
        line_colour_count_maxes = convert_re_matches_to_max_occurrence(re_matches)
        if not max_colours_exceeded(line_colour_count_maxes):
            potential_games.append(index + 1)
    return sum(potential_games)


def multiply_max_occurrences(line_colour_count_maxes: dict[str, int]) -> int:
    """Multiply the max counts of colour occurrences in an input line."""
    return reduce((lambda x, y: x * y), line_colour_count_maxes.values())


def calculate_games_powers_sum(game_records_doc: str) -> int:
    """Trigger extract, transform and calculations. Sum multiplied max occurrences."""
    input_lines = extract_lines(game_records_doc)

    games_powers = []
    for line in input_lines:
        re_matches = extract_colour_counts(line)
        line_colour_count_maxes = convert_re_matches_to_max_occurrence(re_matches)
        games_powers.append(multiply_max_occurrences(line_colour_count_maxes))

    return sum(games_powers)


if __name__ == "__main__":  # pragma: no cover
    game_records_doc = open("./input02.txt", "r").read()
    ans_a = calculate_possible_games_ids_sum(game_records_doc)
    print(f"Answer to first puzzle is: {ans_a}")
    # 53651
    ans_b = calculate_games_powers_sum(game_records_doc)
    print(f"Answer to second puzzle is: {ans_b}")
    # 53894
