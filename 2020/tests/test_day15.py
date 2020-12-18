import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day15 import DAY, run1, run2, get_spoken_number

PUZZLE = """0,3,6"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=DAY)
    expected = 436

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


@pytest.mark.parametrize('starting_numbers,expected', [
    ('1,3,2', 1),
    ('2,1,3', 10),
    ('1,2,3', 27),
    ('2,3,1', 78),
    ('3,2,1', 438),
    ('3,1,2', 1836)
])
def test_get_spoken_number(starting_numbers, expected):
    # Given inputs
    starting_numbers = list(map(int, starting_numbers.split(',')))
    
    # When
    actual = get_spoken_number(starting_numbers, 2020)

    # Then
    assert actual == expected


# def test_run2():
#     # Given
#     day_file_path = write_puzzle(PUZZLE, day=DAY)
#     expected = 175594

#     # When
#     actual = run2(day_file_path)

#     # Then
#     assert actual == expected
