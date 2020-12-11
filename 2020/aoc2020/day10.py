import itertools
import numpy as np


following_ones_arrangements = {
    2: 2,  # [1 1] can also be [2]
    3: 4,  # [1 1 1] can be [2 1], [1 2] or [3]
    4: 7,  # [1 1 1 1] can be [2 1 1], [1 2 1], [1 1 2], [1 3], [3 1] or [2 2]
    5: 18  # [1 1 1 1 1] can be a lot of stuff
}


def _parse(line):
    clean_line = line.strip()
    return int(clean_line)


def get_number_of_arrangements(inputs):
    nb_arrangements = 1
    pointer = 0
    nb_ones = 0
    while pointer < len(inputs):
        i = inputs[pointer]
        if i == 1:
            nb_ones += 1
        else:
            if nb_ones > 1:
                nb_arrangements *= following_ones_arrangements[nb_ones]
            nb_ones = 0
        pointer += 1
    return nb_arrangements
            

def get_jumps(sorted_inputs):
    return [inp - sorted_inputs[i] for i, inp in enumerate(sorted_inputs[1:])]


def run1(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    sorted_inputs = sorted(inputs)
    sorted_inputs_extended = [0] + sorted_inputs + [sorted_inputs[-1] + 3]
    all_jumps = get_jumps(sorted_inputs_extended)
    ones = all_jumps.count(1)
    threes = all_jumps.count(3)
    return ones * threes


def run2(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    sorted_inputs = sorted(inputs)
    sorted_inputs_extended = [0] + sorted_inputs + [sorted_inputs[-1] + 3]
    all_jumps = get_jumps(sorted_inputs_extended)
    return get_number_of_arrangements(all_jumps)
    



if __name__ == '__main__':
    path = 'inputs/day10.txt'
    print("Run 1", run1(path))
    print("Run 2", run2(path))
