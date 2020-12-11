import pytest
import os

from aoc2020.utils import write_puzzle
from aoc2020.day10 import run1, run2

PUZZLE = """16
10
15
5
1
11
7
19
6
12
4"""

PUZZLE_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

@pytest.mark.parametrize("puzzle,expected", [
    (PUZZLE, 35),
    (PUZZLE_2, 220)
])
def test_run1(puzzle, expected):
    # Given
    day_file_path = write_puzzle(puzzle, day=10)

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected

@pytest.mark.parametrize("puzzle,expected", [
    (PUZZLE, 8),
    (PUZZLE_2, 19208)
])
def test_run2(puzzle, expected):
    # Given
    day_file_path = write_puzzle(puzzle, day=10)

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    