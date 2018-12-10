import pandas as pd
import re
import numpy as np
from time import time

from .aoc import AOCDay
from .utils import read_input

pattern = re.compile(r'=\<(.*),(.*)\> .*=\<(.*),(.*)\>')


class Light:

    def __init__(self, x_0, y_0, v_x, v_y):
        self.position = np.array([x_0, y_0])
        self.speed = np.array([v_x, v_y])

    def get_position(self, seconds=0):
        return self.position + seconds * self.speed


class Sky:

    def __init__(self, lights=[]):
        self.lights = lights

    def add_point(self, point):
        self.lights.append(point)

    def get_boundaries(self, seconds=0):
        xs, ys = zip(*map(lambda light: light.get_position(seconds) , self.lights))
        return min(xs), min(ys), max(xs), max(ys)

    def show(self, seconds=0):
        min_x, min_y, max_x, max_y = self.get_boundaries(seconds)
        sky = np.zeros((max_y - min_y+1, max_x-min_x+1))
        for light in self.lights:
            pos_x, pos_y = light.get_position(seconds)
            sky[pos_y-min_y, pos_x-min_x] = 1
        for line in sky:
            print("".join(map(lambda x: "." if x==0 else "#", line)))


class AOCDay10(AOCDay):

    def __init__(self):
        self.day = 10
        self.split_lines = True
        self.second = 0

    def run1(self, inp):
        lights = map(lambda line: Light(*map(int, pattern.findall(line)[0])), inp)
        sky = Sky(list(lights))

        mx, my, Mx, My = sky.get_boundaries(0)
        widths = [Mx-mx]
        heights = [My-my]
        second = 1
        while True:
            mx, my, Mx, My = sky.get_boundaries(second)
            width, height = (Mx - mx, My - my)
            widths.append(width)
            heights.append(height)
            if width > widths[-2] or height > heights[-2]:
                break
            second += 1
        self.second = second-1
        print("Puzzle 1 : ")
        sky.show(self.second)

    def run2(self, inp):
        print("Puzzle 2 : Elves will have to wait %d seconds to read the message." % self.second)

    def execute(self, test=False):
        inp = read_input(self.day, split_lines=self.split_lines, test=test)
        t1 = time()
        self.run1(inp)
        t2 = time()
        self.run2(inp)
        tf = time()
        print("(Puzzle 1 took %0.3fs)" % (t2-t1))
        print("(Puzzle 2 took %0.3fs)" % (tf-t2))
