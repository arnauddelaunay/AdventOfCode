import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day8 import run1, run2

PUZZLE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=3)
    expected = 5

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=3)
    expected = 8

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    