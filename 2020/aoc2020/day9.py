import itertools
import numpy as np


def _parse(line):
    clean_line = line.strip()
    return int(clean_line)


def get_invalid_number(list_of_inputs, n):
    for i, value in enumerate(list_of_inputs[n:]):
        all_pairs = itertools.combinations(list_of_inputs[i: i+n], 2)
        all_sums_of_pairs = list(map(lambda pair: pair[0] + pair[1], all_pairs))
        if value not in all_sums_of_pairs:
            return value
    return None


def get_sum_matrix(list_of_inputs):
    mat = np.zeros((len(list_of_inputs), len(list_of_inputs)))
    for i in range(len(list_of_inputs)):
        for j in range(i+1, len(list_of_inputs)):
            mat[i, j] = sum(list_of_inputs[i:j])
    return mat



def run1(input_path, n=25):
    inputs = list(map(_parse, open(input_path).readlines()))
    return get_invalid_number(inputs, n)


def run2(input_path, n=25):
    inputs = list(map(_parse, open(input_path).readlines()))
    invalid_number = get_invalid_number(inputs, n)
    sum_matrix = get_sum_matrix(inputs)
    i, j = np.argwhere(sum_matrix == invalid_number)[0]
    return max(inputs[i:j]) + min(inputs[i:j])



if __name__ == '__main__':
    path = 'inputs/day9.txt'
    print(run1(path))
    print(run2(path))

    