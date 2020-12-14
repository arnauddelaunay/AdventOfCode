import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day12 import DAY, run1, run2

PUZZLE1 = """F10
N3
F7
R90
F11"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE1, day=DAY)
    expected = 25

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE1, day=DAY)
    expected = 286

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected

