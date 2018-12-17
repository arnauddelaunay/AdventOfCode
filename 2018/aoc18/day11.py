import itertools
import numpy as np

from .aoc import AOCDay


def fuel_level(x, y, inp):
    rack_id = x + 10
    return (((rack_id * y + inp) * rack_id) % 1000) // 100 - 5


class AOCDay11(AOCDay):

    def __init__(self):
        self.day = 11
        self.split_lines = False
        self.size = 300
        self.grid = None

    def fill_grid(self, inp):
        grid_coordinates = itertools.product(range(self.size), range(self.size))
        grid = np.zeros((self.size, self.size))
        for x, y in grid_coordinates:
            grid[x, y] = fuel_level(x, y, inp=inp)
        return grid

    def run1(self, inp):
        inp = int(inp.strip())
        size = self.size
        sub_grid = 3
        grid = self.fill_grid(inp)
        max_total = 0
        answer = (0, 0)
        for x, y in itertools.product(range(size - sub_grid), range(size - sub_grid)):
            this_sub_grid_total = grid[x: x+sub_grid, y: y+sub_grid].sum()
            if max_total < this_sub_grid_total:
                max_total = this_sub_grid_total
                answer = (x, y)
        return ",".join(map(str, answer))

    def run2(self, inp):
        inp = int(inp.strip())
        grid = self.fill_grid(inp)
        cache = np.zeros((self.size, self.size, self.size))
        cache[:, :, 1] = grid

        def get_sub_total(x, y, s):
            if s == 1:
                return cache[x, y, 1]
            else:
                return cache[x, y, s-1] + grid[x+s, y:y+s-1].sum() + grid[x:x+s, y+s].sum()

        max_total = 0
        answer = (0, 0, 1)
        for sub_grid in range(1, self.size):
            for x, y in itertools.product(range(self.size - sub_grid), range(self.size - sub_grid)):
                this_sub_grid_total = get_sub_total(x, y, sub_grid)
                cache[x, y, sub_grid] = this_sub_grid_total
                if max_total < this_sub_grid_total:
                    max_total = this_sub_grid_total
                    answer = (x, y, sub_grid)
        return ",".join(map(str, answer))
