import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day16 import DAY, run1, run2

PUZZLE1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

PUZZLE2 = """departure1: 0-1 or 4-19
departure2: 0-5 or 8-19
departure3: 0-13 or 16-19
seat: 70-72 or 75-80

your ticket:
11,12,13,71

nearby tickets:
3,9,18,76
15,1,5,77
5,14,18,78"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE1, day=DAY)
    expected = 71

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE2, day=DAY)
    expected = 11*12*13

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
