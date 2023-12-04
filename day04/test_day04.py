import os

from day04.day04 import calculate_scratchcard_points

current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)

example_doc = open(os.path.join(current_directory, "example.txt"), "r").read()


def test_calculate_scratchard_points():
    assert (calculate_scratchcard_points(example_doc)) == 13
