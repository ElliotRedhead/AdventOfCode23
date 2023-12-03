import os

import pytest

from day03.day03 import extract_row_index_num_strs, is_value_integer, sum_part_numbers

current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)

example_doc = open(os.path.join(current_directory, "example.txt"), "r").read()


@pytest.mark.parametrize(
    ("char", "expected"),
    [
        pytest.param("1", True),
        pytest.param(".", False),
        pytest.param("$", False),
    ],
)
def test_is_value_integer(char, expected):
    assert is_value_integer(char) == expected


@pytest.mark.parametrize(
    ("row", "expected"),
    [
        pytest.param(
            "467..114..", [{0: "4", 1: "6", 2: "7"}, {5: "1", 6: "1", 7: "4"}]
        ),
        pytest.param("...*......", []),
        pytest.param("..35..633.", [{2: "3", 3: "5"}, {6: "6", 7: "3", 8: "3"}]),
        pytest.param("......#...", []),
        pytest.param("617*......", [{0: "6", 1: "1", 2: "7"}]),
        pytest.param(".....+.58.", [{7: "5", 8: "8"}]),
        pytest.param("..592.....", [{2: "5", 3: "9", 4: "2"}]),
        pytest.param("......755.", [{6: "7", 7: "5", 8: "5"}]),
        pytest.param("...$.*....", []),
        pytest.param(
            ".664.598..", [{1: "6", 2: "6", 3: "4"}, {5: "5", 6: "9", 7: "8"}]
        ),
    ],
)
def test_extract_row_index_num_strs(row, expected):
    assert extract_row_index_num_strs(row) == expected


def test_sum_part_numbers():
    assert sum_part_numbers(example_doc) == 4361
