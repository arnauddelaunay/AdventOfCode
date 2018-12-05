from .utils import read_input
from time import time


class AOCDay:

    def __init__(self, day=None, split_lines=True):
        self.day = day
        self.split_lines = split_lines

    def execute(self, test=False):
        inp = read_input(self.day, split_lines=self.split_lines, test=test)
        t1 = time()
        res1 = self.run1(inp)
        t2 = time()
        res2 = self.run2(inp)
        tf = time()
        out1 = " not implemented yet." if res1 is None else " : %s" % res1
        out2 = " not implemented yet." if res2 is None else " : %s" % res2
        print("Puzzle 1%s (took %0.3fs)" % (out1, t2-t1))
        print("Puzzle 2%s (took %0.3fs)" % (out2, tf-t2))

    def run1(self, inp):
        """
        Method to override
        """
        return None

    def run2(self, inp):
        """
        Method to override
        """
        return None