import numpy as np

from .aoc import AOCDay


def get_sign(c):
    return 1 if c == "+" else -1


class AOCDay1(AOCDay):

    def __init__(self):
        self.day = 1

    def run1(self, inp):
        self.inp = list(map(lambda x: get_sign(x[0])*int(x[1:]), inp))
        return sum(self.inp)

    def run2(self, inp):
        this_sum = 0
        results = set([this_sum])
        i = 0
        while True:
            this_sum += self.inp[i]
            if this_sum in results:
                break
            results.add(this_sum)
            i = np.mod(i+1, len(self.inp))
        return this_sum
