import os

import pytest

from day04.day04 import (
    calculate_line_points,
    calculate_scratchcards_points,
    extract_numbers,
    intersecting_list_values,
)

current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)

example_doc = open(os.path.join(current_directory, "example.txt"), "r").read()


@pytest.mark.parametrize(
    ("scratch_line", "expected"),
    [
        pytest.param(
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]],
        )
    ],
)
def test_extract_numbers(scratch_line, expected):
    assert extract_numbers(scratch_line) == expected


def test_intersecting_list_values():
    list_one = [41, 48, 83, 86, 17]
    list_two = [83, 86, 6, 31, 17, 9, 48, 53]
    assert (intersecting_list_values(list_one, list_two)) == [48, 17, 83, 86]


@pytest.mark.parametrize(
    ("intersecting_count", "expected"),
    [
        pytest.param(0, 0),
        pytest.param(1, 1),
        pytest.param(2, 2),
        pytest.param(3, 4),
        pytest.param(4, 8),
        pytest.param(5, 16),
        pytest.param(6, 32),
        pytest.param(7, 64),
        pytest.param(8, 128),
    ],
)
def test_calculate_line_points(intersecting_count, expected):
    assert (calculate_line_points(intersecting_count)) == expected


def test_calculate_scratchard_points():
    assert (calculate_scratchcards_points(example_doc)) == 13
