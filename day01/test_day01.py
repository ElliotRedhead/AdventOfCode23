import os

import pytest

from day01.day01 import (
    calibrate_trebuchet,
    combine_extracted_num_strs,
    extract_lines,
    extract_num_strs,
)

current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)

example_doc_one = open(os.path.join(current_directory, "example1.txt"), "r").read()
example_doc_two = open(os.path.join(current_directory, "example2.txt"), "r").read()


@pytest.mark.parametrize(
    ("example_doc", "expected"),
    [
        pytest.param(
            example_doc_one,
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ],
        ),
        pytest.param(
            example_doc_two,
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
        ),
    ],
)
def test_extract_lines(example_doc, expected):
    assert (extract_lines(example_doc)) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        pytest.param("1abc2", ["1", "2"]),
        pytest.param("pqr3stu8vwx", ["3", "8"]),
        pytest.param("a1b2c3d4e5f", ["1", "5"]),
        pytest.param("treb7uchet", ["7", "7"]),
        pytest.param("two1nine", ["2", "9"]),
        pytest.param("eightwothree", ["8", "3"]),
        pytest.param("abcone2threexyz", ["1", "3"]),
        pytest.param("xtwone3four", ["2", "4"]),
        pytest.param("4nineeightseven2", ["4", "2"]),
        pytest.param("zoneight234", ["1", "4"]),
        pytest.param("7pqrstsixteen", ["7", "6"]),
    ],
)
def test_all_numbers_extracted_from_string(line: str, expected: list[int]):
    assert extract_num_strs(line, True) == expected


@pytest.mark.parametrize(
    ("extracted_num_strs", "expected"),
    [
        pytest.param(["1", "2"], 12),
        pytest.param(["3", "8"], 38),
        pytest.param(["1", "5"], 15),
        pytest.param(["7", "7"], 77),
    ],
)
def test_combine_extracted_num_strs(extracted_num_strs: list[str], expected: int):
    assert (combine_extracted_num_strs(extracted_num_strs)) == expected


@pytest.mark.parametrize(
    ("input_doc", "alternative_str_nums", "expected"),
    [
        pytest.param(example_doc_one, False, 142),
        pytest.param(example_doc_two, True, 281),
    ],
)
def test_calibrate_trebuchet(input_doc, alternative_str_nums, expected):
    assert (calibrate_trebuchet(input_doc, alternative_str_nums)) == expected
