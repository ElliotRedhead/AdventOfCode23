import regex as re

num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_lines(input: str):
    split = input.split("\n")
    return split


def extract_num_strs(line: str, alternative_str_nums: bool) -> list[str] | None:
    """
    Extract first and last numbers from parsed line

    e.g. with alternatives: "two1nine" -> ["2", "9"].
    e.g. without alternatives: "two1nine" -> ["1"]
    """
    valid_str_alternative_re: str = "|".join([key for key in num_map.keys()])
    if alternative_str_nums:
        all_nums = re.findall(
            f"[0-9]|{valid_str_alternative_re}", line, overlapped=True
        )
    else:
        all_nums = re.findall("[0-9]", line)

    all_nums = [(num) for num in all_nums]
    target_nums = [all_nums[0], all_nums[-1]]
    for index, num_str in enumerate(target_nums):
        if num_str in num_map:
            target_nums[index] = num_map[num_str]

    return target_nums


def combine_extracted_num_strs(num_strs: list[str]) -> int:
    """Concatenate integers cast as strings and cast to int. e.g. ["2", "9"] -> 29"""
    return int(num_strs[0] + num_strs[1])


def calibrate_trebuchet(calibration_doc: str, alternative_str_nums: bool) -> int:
    """Trigger file parsing and calcs, form running total of extracted numbers."""
    input_lines = extract_lines(calibration_doc)
    calibration_value = 0
    for line in input_lines:
        extracted_num_strs = extract_num_strs(line, alternative_str_nums)
        if extracted_num_strs is not None:
            calibration_value += combine_extracted_num_strs(extracted_num_strs)
    return calibration_value


if __name__ == "__main__":  # pragma: no cover
    calibration_doc_one = open("./input1.txt", "r").read()
    ans_one = calibrate_trebuchet(calibration_doc_one, False)
    print(f"Answer to first puzzle is: {ans_one}")
    # 53651
    calibration_doc_two = open("./input2.txt", "r").read()
    ans_two = calibrate_trebuchet(calibration_doc_two, True)
    print(f"Answer to second puzzle is: {ans_two}")
    # 53894
