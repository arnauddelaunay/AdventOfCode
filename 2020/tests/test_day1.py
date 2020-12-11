import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day1 import run1, run2

PUZZLE = """1721
979
366
299
675
1456"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=1)
    expected = 514579

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=1)
    expected = 241861950

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    