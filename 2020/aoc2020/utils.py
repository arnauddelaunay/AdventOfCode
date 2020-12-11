import os

from aoc2020.constants import TEST_DATA_PATH


def write_puzzle(puzzle, day=1):
    day_file_path = os.path.join(TEST_DATA_PATH, "day%d.txt" % day)
    with open(day_file_path, 'w') as day_file:
        day_file.write(puzzle)
    return day_file_path
