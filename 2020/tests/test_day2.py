import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day2 import run1, run2

PUZZLE = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=2)
    expected = 2

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=1)
    expected = 1

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    