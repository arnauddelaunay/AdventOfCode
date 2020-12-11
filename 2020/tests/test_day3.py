import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day3 import run1, run2

PUZZLE = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=3)
    expected = 7

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=3)
    expected = 336

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    