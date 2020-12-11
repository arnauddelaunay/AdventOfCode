import numpy as np

TREE = '#'
OPEN = '.'


def _get_map(inputs, step):
    array_input = np.array([list(inp.strip()) for inp in inputs])
    n_cols_needed = array_input.shape[0] * step[1]/step[0]
    while array_input.shape[1] < n_cols_needed:
        array_input = np.hstack([array_input]*2)
    return array_input


def run1(input_path, step=(1, 3)):
    inputs = list(map(lambda x: x.strip(), open(input_path).readlines()))
    this_map = _get_map(inputs, step)
    lines = list(range(0, this_map.shape[0], step[0]))
    cols = list(range(0, this_map.shape[1], step[1]))
    counter = {OPEN: 0, TREE: 0}
    for i, j in zip(lines, cols):
        counter[this_map[i, j]] += 1
    return counter[TREE]


def run2(input_path):
    trees = 1
    for step in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        nb_tree = run1(input_path, step)
        trees *= nb_tree
    return trees



if __name__ == '__main__':
    path = 'inputs/day3.txt'
    print(run1(path))
    print(run2(path))
