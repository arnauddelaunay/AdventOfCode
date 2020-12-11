import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day11 import _get_adjacent_seats, _get_visible_seats, run1, run2

PUZZLE = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

@pytest.mark.parametrize('i,j,expected', [
    (0, 0, ['.', 'L', 'L']),
    (2, 1, ['L']*8)
])
def test__get_adjacent_seats(i, j, expected):
    # Given
    array = np.array(list(map(lambda line: [c for c in line], PUZZLE.split('\n'))))

    # When
    actual = _get_adjacent_seats(array, i, j)

    # Then
    assert actual == expected


@pytest.mark.parametrize('i,j,expected', [
    (4, 3, 8),
    (2, 8, 2)
])
def test__get_visible_seats(i, j, expected):
    # Given
    array_str = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    array = np.array(list(map(lambda line: [c for c in line], array_str.split('\n'))))

    # When
    actual = _get_visible_seats(array, i, j)

    # Then
    assert actual == expected


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=11)
    expected = 37

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=11)
    expected = 26

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
    