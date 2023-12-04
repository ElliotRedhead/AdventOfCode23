import os

import regex as re


def extract_rows(input: str) -> list[str]:
    split = input.split("\n")
    return split


def extract_numbers(line: str) -> list[list[int]]:
    matches = re.compile(r"\b(\d{1,2})\s?|\|").findall(line)
    matches.pop(0)

    parsed_scratchcard: list[list[int]] = [[], []]
    target_array = 0
    for match in matches:
        try:
            scratch_num = int(match)
        except ValueError:
            target_array = 1
            continue
        parsed_scratchcard[target_array].append(int(scratch_num))
    return parsed_scratchcard


def intersecting_list_values(list_one: list, list_two: list) -> list:
    return list(set(list_one) & set(list_two))


def calculate_line_points(intersecting_count: int) -> int:
    line_score = 0
    if intersecting_count == 1:
        line_score = 1
    if intersecting_count > 1:
        line_score = 1
        for _ in range(intersecting_count - 1):
            line_score = line_score * 2
    return line_score


def calculate_scratchcards_points(scratchcards_file) -> int:
    lines: list[str] = extract_rows(scratchcards_file)

    total_score = 0
    for _, line in enumerate(lines):
        scratch_nums = extract_numbers(line)
        intersecting_values = intersecting_list_values(scratch_nums[0], scratch_nums[1])
        scratchcard_score = calculate_line_points(len(intersecting_values))
        total_score += scratchcard_score

    return total_score


if __name__ == "__main__":  # pragma: no cover
    current_file_path = os.path.realpath(__file__)
    current_directory = os.path.dirname(current_file_path)
    scratchcards_file = open(os.path.join(current_directory, "input.txt"), "r").read()
    ans_one = calculate_scratchcards_points(scratchcards_file)
    print(f"Answer to first puzzle is: {ans_one}")  # 20855
