import itertools
import numpy as np

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def _parse(line):
    clean_line = line.strip()
    return [c for c in clean_line]


def _get_adjacent_seats(array, i, j):
    adjacents = []
    for k in range(-1, 2):
        for p in range(-1, 2):
            if k == p == 0:
                continue
            if ((i+k >= 0) and (i+k < array.shape[0])
                and (j+p >= 0) and (j+p < array.shape[1])):
                adjacents.append(array[i+k, j+p])
    return adjacents


def _get_visible_seats(array, i, j):
    def _inbound_condition(i, j, k, p, step, shape):
        return ((i+k*step >= 0) and (i+k*step < shape[0])
                and (j+p*step >= 0) and (j+p*step < shape[1]))
    count = 0
    for k in range(-1, 2):
        for p in range(-1, 2):
            if k == p == 0:
                continue
            step = 1
            inbound_condition = _inbound_condition(i, j, k, p, step, array.shape)
            while inbound_condition:
                visible_status = array[i+k*step, j+p*step]
                if visible_status != FLOOR:
                    break
                step += 1
                inbound_condition = _inbound_condition(i, j, k, p, step, array.shape)
            if inbound_condition and visible_status == OCCUPIED:
                count += 1
    return count
            

def apply_rule1(array):
    new_array = array.copy()
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            status = array[i, j]
            adjacents = _get_adjacent_seats(array, i, j)
            if (status == EMPTY) and (OCCUPIED not in adjacents):
                new_array[i, j] = OCCUPIED
            if (status == OCCUPIED) and (adjacents.count(OCCUPIED) >= 4):
                new_array[i, j] = EMPTY
    return new_array


def apply_rule2(array):
    new_array = array.copy()
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            status = array[i, j]
            nb_visible = _get_visible_seats(array, i, j)
            if (status == EMPTY) and (nb_visible == 0):
                new_array[i, j] = OCCUPIED
            if (status == OCCUPIED) and (nb_visible >= 5):
                new_array[i, j] = EMPTY
    return new_array


def run1(input_path):
    array = np.array(list(map(_parse, open(input_path).readlines())))
    new_array = apply_rule1(array)
    while not np.array_equal(array, new_array):
        array = new_array
        new_array = apply_rule1(array)
    return (new_array == OCCUPIED).sum()


def run2(input_path):
    array = np.array(list(map(_parse, open(input_path).readlines())))
    new_array = apply_rule2(array)
    while not np.array_equal(array, new_array):
        array = new_array
        new_array = apply_rule2(array)
    return (new_array == OCCUPIED).sum()
    



if __name__ == '__main__':
    path = 'inputs/day11.txt'
    print("Run 1", run1(path))
    print("Run 2", run2(path))
