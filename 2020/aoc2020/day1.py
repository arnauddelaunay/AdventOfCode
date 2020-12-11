import itertools


def run1(input_path):
    inputs = list(map(lambda x: int(x.strip()), open(input_path).readlines()))
    all_tuples = itertools.combinations(inputs, 2)
    for a, b in all_tuples:
        if a + b == 2020:
            return a*b


def run2(input_path):
    inputs = list(map(lambda x: int(x.strip()), open(input_path).readlines()))
    all_triples = itertools.combinations(inputs, 3)
    for a, b, c in all_triples:
        if a + b + c == 2020:
            return a*b*c


if __name__ == '__main__':
    path = 'inputs/day1.txt'
    print(run1(path))
    print(run2(path))
