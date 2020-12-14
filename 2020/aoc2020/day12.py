import re

DAY = 12

CARDINALS = 'NESW'
MOVES = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 1),
    'W': (1, -1)
}

def _parse(line):
    clean_line = line.strip()
    pattern = r'^([NSEWLRF])(\d+)$'
    matches = re.findall(pattern, clean_line)[0]
    return (matches[0], int(matches[1]))


def run1(input_path):
    position = [0, 0]
    direction = 'E'
    for instruction, value in map(_parse, open(input_path).readlines()):
        if instruction in CARDINALS:
            position[MOVES[instruction][0]] += MOVES[instruction][1] * value
        if instruction == 'R':
            n = value//90
            direction = CARDINALS[(CARDINALS.index(direction) + n) % 4]
        if instruction == 'L':
            n = value//90
            direction = CARDINALS[(CARDINALS.index(direction) - n) % 4]
        if instruction == 'F':
            position[MOVES[direction][0]] += MOVES[direction][1] * value
    return abs(position[0]) + abs(position[1])


def run2(input_path):
    boat_position = [0, 0]
    waypoint_position = [1, 10]
    for instruction, value in map(_parse, open(input_path).readlines()):
        if instruction in CARDINALS:
            waypoint_position[MOVES[instruction][0]] += MOVES[instruction][1] * value
        if instruction in 'LR':
            n = value//90
            angle_sign = 1 if instruction == 'R' else -1
            if n == 1:
                new_position = [-angle_sign*waypoint_position[1], angle_sign*waypoint_position[0]]
            if n == 2:
                new_position = [-waypoint_position[0], -waypoint_position[1]]
            if n == 3:
                new_position = [angle_sign*waypoint_position[1], -angle_sign*waypoint_position[0]]
            waypoint_position = new_position
        if instruction == 'F':
            for i in range(2):
                boat_position[i] += waypoint_position[i]*value
    return abs(boat_position[0]) + abs(boat_position[1])
    



if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
