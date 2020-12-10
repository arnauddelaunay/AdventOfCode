import itertools


def run1(input_path):
    inputs = list(map(lambda x: int(x.strip()), open(input_path).readlines()))
    all_tuples = itertools.combinations(inputs, 2)
    for a, b in all_tuples:
        if a + b == 2020:
            print(a, b, a+b, a*b)
            return a*b


def run2(input_path):
    inputs = list(map(lambda x: int(x.strip()), open(input_path).readlines()))
    all_triples = itertools.combinations(inputs, 3)
    for a, b, c in all_triples:
        if a + b + c == 2020:
            print(a, b, c, a+b+c, a*b*c)
            return a*b*c


if '__name__' == '__main__':
    path = '/c/Users/arnaud_delaunay/workspace/Perso/adventofcode/inputs/day1.txt'
    run1(path)
    run2(path)
