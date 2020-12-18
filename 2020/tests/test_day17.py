import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day17 import DAY, run1, run2

PUZZLE = """.#.
..#
###"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=DAY)
    expected = 112

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


# def test_run2():
#     # Given
#     day_file_path = write_puzzle(PUZZLE, day=DAY)
#     expected = 848

#     # When
#     actual = run2(day_file_path)

#     # Then
#     assert actual == expected
    