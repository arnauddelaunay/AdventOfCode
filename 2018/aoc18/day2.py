from collections import Counter
from .aoc import AOCDay


def get_count_of_2_and_3(values):
    c2 = 2 in values
    c3 = 3 in values
    return c2, c3


def compare_without_idx(inp, i):
    inputs = Counter(map(lambda x: x[:i] + x[(i+1):], inp))
    if 2 in inputs.values():
        return inputs.most_common(1)[0][0]


class AOCDay2(AOCDay):

    def __init__(self):
        self.day = 2
        self.split_lines = True

    def run1(self, inp):
        c2s, c3s = zip(*map(lambda x: get_count_of_2_and_3(Counter(x).values()), inp))
        return sum(c2s) * sum(c3s)

    def run2(self, inp):
        for i in range(len(inp[0])):
            c = compare_without_idx(inp, i)
            if c is not None:
                break
        return c.strip()
