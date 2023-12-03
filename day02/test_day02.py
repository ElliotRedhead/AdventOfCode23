import os

import pytest

from day02.day02 import (
    calculate_games_powers_sum,
    calculate_possible_games_ids_sum,
    convert_re_matches_to_max_occurrence,
    extract_colour_counts,
    extract_lines,
    max_colours_exceeded,
    multiply_max_occurrences,
)

current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)

example_doc = open(os.path.join(current_directory, "example.txt"), "r").read()


@pytest.mark.parametrize(
    ("example_doc", "expected"),
    [
        pytest.param(
            example_doc,
            [
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ],
        )
    ],
)
def test_extract_lines(example_doc, expected):
    assert (extract_lines(example_doc)) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        pytest.param(
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            [
                ("3 blue", "3", "blue"),
                ("4 red", "4", "red"),
                ("1 red", "1", "red"),
                ("2 green", "2", "green"),
                ("6 blue", "6", "blue"),
                ("2 green", "2", "green"),
            ],
        )
    ],
)
def test_extract_colour_counts(line: str, expected: list[set[str]]):
    assert extract_colour_counts(line) == expected


@pytest.mark.parametrize(
    ("re_matches", "expected"),
    [
        pytest.param(
            [
                ("3 blue", "3", "blue"),
                ("4 red", "4", "red"),
                ("1 red", "1", "red"),
                ("2 green", "2", "green"),
                ("6 blue", "6", "blue"),
                ("2 green", "2", "green"),
            ],
            {
                "blue": 6,
                "red": 4,
                "green": 2,
            },
        ),
    ],
)
def test_convert_rematches_to_max_occurrence(re_matches, expected):
    assert convert_re_matches_to_max_occurrence(re_matches) == expected


@pytest.mark.parametrize(
    ("colour_counts", "expected"),
    [
        pytest.param(({"red": 11, "green": 12, "blue": 13}), False),
        pytest.param(({"red": 12, "green": 13, "blue": 14}), False),
        pytest.param(({"red": 13, "green": 13, "blue": 14}), True),
        pytest.param(({"red": 12, "green": 14, "blue": 14}), True),
        pytest.param(({"red": 12, "green": 13, "blue": 15}), True),
    ],
)
def test_max_colours_exceeded(colour_counts, expected):
    """
    Do any of the counts exceed the preset count depicted by the colour_counts_limits.
    {"red": 12, "green": 13, "blue": 14}
    """
    assert max_colours_exceeded(colour_counts) == expected


def test_calculate_possible_games_ids_sum():
    assert calculate_possible_games_ids_sum(example_doc) == 8


@pytest.mark.parametrize(
    ("line_colour_count_maxes", "expected"),
    [
        pytest.param({"red": 4, "green": 2, "blue": 6}, 48),
        pytest.param({"red": 1, "green": 3, "blue": 4}, 12),
        pytest.param({"red": 20, "green": 13, "blue": 6}, 1560),
        pytest.param({"red": 14, "green": 3, "blue": 15}, 630),
        pytest.param({"red": 6, "green": 3, "blue": 2}, 36),
    ],
)
def test_multiply_max_occurrences(line_colour_count_maxes, expected):
    assert multiply_max_occurrences(line_colour_count_maxes) == expected


def test_calculate_games_powers_sum():
    assert calculate_games_powers_sum(example_doc) == 2286
