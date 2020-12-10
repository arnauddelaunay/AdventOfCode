import re


def _parse(line):
    clean_line = line.strip()
    row = clean_line[:-3].replace('B', '1').replace('F', '0')
    column = clean_line[-3:].replace('R', '1').replace('L', '0')
    return int(row, 2), int(column, 2)


def run1(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    seat_ids = list(map(lambda rc: 8*rc[0] + rc[1], inputs)) 
    return max(seat_ids)


def run2(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    seat_ids = list(map(lambda rc: 8*rc[0] + rc[1], inputs))
    for i in range(max(seat_ids)):
        if ((i-1) in seat_ids) and ((i+1) in seat_ids) and (i not in seat_ids):
            return(i)


if __name__ == '__main__':
    path = 'inputs/day5.txt'
    print(run1(path))
    print(run2(path))

    