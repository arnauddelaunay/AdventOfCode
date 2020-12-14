import pytest
import numpy as np

from aoc2020.utils import write_puzzle
from aoc2020.day13 import DAY, run1, run2, get_first_timestamp

PUZZLE = """939
7,13,x,x,59,x,31,19"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=DAY)
    expected = 295

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


@pytest.mark.parametrize('bus_ids,expected_timestamp', [
    ('17,x,13,19', 3417),
    ('67,7,59,61', 754018),
    ('67,x,7,59,61', 779210),
    ('67,7,x,59,61', 1261476),
    ('1789,37,47,1889', 1202161486)
])
def test_get_first_timestamp(bus_ids, expected_timestamp):
    # Given inputs
    buses = {}
    for i, b_id in enumerate(bus_ids.split(',')):
        if b_id != 'x':
            buses[int(b_id)] = i

    # When
    actual_timestamp = get_first_timestamp(buses)

    # Then
    assert actual_timestamp == expected_timestamp


def test_run2():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=DAY)
    expected = 1068781

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
