import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day6 import run1, run2

PUZZLE = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=6)
    expected = 11

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=6)
    expected = 6

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    