import pytest
import re

from aoc2020.utils import write_puzzle
from aoc2020.day18 import DAY, run1, run2, _parse, get_result, split_elements_and_operators, add_prevalence

PUZZLE = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


def test_run1():
    # Given
    day_file_path = write_puzzle(PUZZLE, day=DAY)
    expected = 13632

    # When
    actual = run1(day_file_path)

    # Then
    assert actual == expected


@pytest.mark.parametrize('operation_str,expected', [
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('(((5 + 9) + 6) + 6)', 26)
])
def test_get_result(operation_str, expected):
    # Given inputs
    elements, operators = _parse(operation_str)
    
    # When
    actual = get_result(elements, operators)

    # Then
    assert actual == expected


@pytest.mark.parametrize('operation_str,expected_elements,expected_operators', [
    ('1 + 2 * 3 + 4 * 5 + 6', 
        [('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0)], 
         [('+', 0), ('*', 0), ('+', 0), ('*', 0), ('+', 0)]),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 
        [('2', 2), ('4', 2), ('9', 2), ('6', 2), ('9', 2), ('8', 2), ('6', 2), ('6', 1), ('2', 0), ('4', 0), ('2', 0)], 
         [('+', 2), ('*', 2), ('*', 1), ('+', 2), ('*', 2), ('+', 2), ('+', 1), ('+', 0), ('+', 0), ('*', 0)]),
    ('((5 + 9) + 6) + 6',
        [('5', 2), ('9', 2), ('6', 1), ('6', 0)],
        [('+', 2), ('+', 1), ('+', 0)])
])
def test_split_elements_and_operators(operation_str,expected_elements,expected_operators):
    # Given inputs
    elements_and_operators = re.findall(r'([()*+]|\d+)', operation_str)

    # When
    actual_elements, actual_operators = split_elements_and_operators(elements_and_operators)

    # Then
    assert actual_elements == expected_elements
    assert actual_operators == expected_operators


@pytest.mark.parametrize('elements,operators,expected_elements,expected_operators', [
    (
        [('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0)], 
        [('+', 0), ('*', 0), ('+', 0), ('*', 0), ('+', 0)],
        [('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1)], 
        [('+', 1), ('*', 0), ('+', 1), ('*', 0), ('+', 1)]
    ),
    (
        [('2', 2), ('4', 2), ('9', 2), ('6', 2), ('9', 2), ('8', 2), ('6', 2), ('6', 1), ('2', 0), ('4', 0), ('2', 0)], 
        [('+', 2), ('*', 2), ('*', 1), ('+', 2), ('*', 2), ('+', 2), ('+', 1), ('+', 0), ('+', 0), ('*', 0)],
        [('2', 5), ('4', 5), ('9', 4), ('6', 6), ('9', 6), ('8', 6), ('6', 6), ('6', 4), ('2', 2), ('4', 1), ('2', 0)], 
        [('+', 5), ('*', 4), ('*', 3), ('+', 6), ('*', 5), ('+', 6), ('+', 4), ('+', 2), ('+', 1), ('*', 0)]
    ),
    (
        [('5', 2), ('9', 2), ('6', 1), ('6', 0)],
        [('+', 2), ('+', 1), ('+', 0)],
        [('5', 5), ('9', 5), ('6', 3), ('6', 1)],
        [('+', 5), ('+', 3), ('+', 1)]
    )
])
def test_add_prevalence(elements, operators, expected_elements, expected_operators):
    #Given inputs

    # When
    actual_elements, actual_operators = add_prevalence(elements, operators)

    # Then
    assert actual_elements == expected_elements
    assert actual_operators == expected_operators



@pytest.mark.parametrize('puzzle,expected', [
    ('2 * 3 + (4 * 5)', 46),
    ('2 + 4 * 9', 54),
    ('6 + 9 * 8 + 6', 210),
    ('(2 + 4 * 9) * (6 + 9 * 8 + 6) + 6', 11664),
    (PUZZLE, 23340),
])
def test_run2(puzzle, expected):
    # Given
    day_file_path = write_puzzle(puzzle, day=DAY)

    # When
    actual = run2(day_file_path)

    # Then
    assert actual == expected
