import os

import regex as re


def extract_rows(input: str):
    split = input.split("\n")
    return split


def is_value_integer(file_char: str):
    return bool(re.match("[0-9]", file_char))


def extract_row_index_num_strs(row: str) -> list[dict[int, str]]:
    index_num_strs: dict[int, str] = {}  # int_index, str
    row_index_num_strs: list[dict[int, str]] = []

    for x_index, char in enumerate(row):
        # We don't need to re-check the same x_indices
        if x_index in index_num_strs:
            continue
        index_num_strs = {}
        if is_value_integer(char):
            index_num_strs[x_index] = char
            neighbour_char_offset = 1
            while True:
                neighbour_index = x_index + neighbour_char_offset
                if neighbour_index < len(row):
                    if is_value_integer(row[neighbour_index]):
                        index_num_strs[neighbour_index] = row[neighbour_index]
                        neighbour_char_offset += 1
                    else:
                        row_index_num_strs.append(index_num_strs)
                        break
                else:
                    row_index_num_strs.append(index_num_strs)
                    break
    return row_index_num_strs


def is_trigger_symbol(char: str) -> bool:
    is_trigger = bool(not re.match("[0-9.]", char))
    return is_trigger


def has_adjacent_symbol(grid: list[str], y_index: int, x_indices: list[int]):
    max_grid_x = len(grid[0])
    max_grid_y = len(grid) - 1

    x_neg_offset_limit = 1 if min(x_indices) > 0 else 0
    x_pos_offset_limit = 1 if max(x_indices) + 1 < max_grid_x else 0
    for x_index in range(
        min(x_indices) - x_neg_offset_limit, max(x_indices) + 1 + x_pos_offset_limit
    ):
        if y_index > 0 and is_trigger_symbol(grid[y_index - 1][x_index]):
            return True

        if x_index not in x_indices and is_trigger_symbol(grid[y_index][x_index]):
            return True

        if y_index < max_grid_y - 1 and is_trigger_symbol(grid[y_index + 1][x_index]):
            return True

    return False


def combine_extracted_num_strs(num_strs: list[str]) -> str:
    """Concatenate integers cast as strings. e.g. ["2", "9"] -> 29"""
    combined_num_str = ""
    for num_str in num_strs:
        combined_num_str = combined_num_str + num_str
    return combined_num_str


def sum_part_numbers(schematic_file) -> int:
    grid = extract_rows(schematic_file)
    engine_part_numbers = []
    for y_index, row in enumerate(grid):
        row_index_num_strs = extract_row_index_num_strs(row)
        for row_index_num_str in row_index_num_strs:
            if has_adjacent_symbol(grid, y_index, list(row_index_num_str.keys())):
                engine_part_numbers.append(
                    int(combine_extracted_num_strs(list(row_index_num_str.values())))
                )
    return sum(engine_part_numbers)


if __name__ == "__main__":  # pragma: no cover
    current_file_path = os.path.realpath(__file__)
    current_directory = os.path.dirname(current_file_path)
    schematic_file = open(os.path.join(current_directory, "input.txt"), "r").read()
    ans_one = sum_part_numbers(schematic_file)
    print(f"Answer to first puzzle is: {ans_one}")
