import argparse

from aoc18 import days

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Execute AOC - 2018')
    parser.add_argument('-d', '--day', help="day number", type=int)
    parser.add_argument('-t', '--test', help='weither to run on test or not', type=bool, default=False)
    args = parser.parse_args()

    days[args.day].execute(test=args.test)


