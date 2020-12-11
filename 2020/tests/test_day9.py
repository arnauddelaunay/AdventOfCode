import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day9 import run1, run2

PUZZLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=9)
    n = 5
    expected = 127

    # When
    actual = run1(day_file_path, n=n)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=9)
    n = 5
    expected = 62

    # When
    actual = run2(day_file_path, n=n)

    # Then
    assert actual == expected
    