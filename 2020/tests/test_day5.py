import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day5 import run1

PUZZLE = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=5)
    expected = 820

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected
    