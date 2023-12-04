import os

import regex as re


def extract_rows(input: str) -> list[str]:
    split = input.split("\n")
    return split


def extract_numbers(line: str) -> list[str]:
    matches = re.compile(r"\b(\d{1,2})\s").findall(line)
    nums = []
    for match in matches:
        nums.append(int(match))

    return matches


def calculate_scratchcard_points(scratchcards_file) -> int:
    sum_points: int = 0
    lines: list[str] = extract_rows(scratchcards_file)
    separator_index: int = lines[0].find("|")

    for line in lines:
        extract_numbers(line)

    return sum_points


if __name__ == "__main__":  # pragma: no cover
    current_file_path = os.path.realpath(__file__)
    current_directory = os.path.dirname(current_file_path)
    scratchcards_file = open(os.path.join(current_directory, "example.txt"), "r").read()
    ans_one = calculate_scratchcard_points(scratchcards_file)
    print(f"Answer to first puzzle is: {ans_one}")
