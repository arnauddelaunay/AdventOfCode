import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day14 import DAY, run1, run2

PUZZLE1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

PUZZLE2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE1, day=DAY)
    expected = 165

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE2, day=DAY)
    expected = 208

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
