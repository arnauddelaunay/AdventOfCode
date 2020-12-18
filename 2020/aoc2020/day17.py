import itertools
import numpy as np
import copy

DAY = 17
ACTIVE = "#"
INACTIVE = "."


def _parse(lines, dimension=3):
    active_cubes = []
    for i, line in enumerate(lines):
        clean_line = line.strip()
        for j, cube in enumerate(clean_line):
            if cube == ACTIVE:
                cube_coordinate = np.hstack([np.array([i, j]), np.zeros(dimension-2)]).astype(int)
                active_cubes.append(cube_coordinate)
    return active_cubes


def _get_adjacent_coordinates(coordinate, dimension=3):
    adjacents = []
    offsets = set([p 
        for c in itertools.combinations_with_replacement([-1, 0, 1], dimension) 
        for p in itertools.permutations(c)
    ])
    for offset in offsets:
        offset = np.array(offset)
        if (offset == 0).all():
            continue
        else:
            neighbor_cube_coordinate = coordinate + offset
            adjacents.append(neighbor_cube_coordinate)
    return adjacents
    
    
def _get_nb_adjacent_active(coordinate, active_cubes, dimension=3):
    adjacents_active_cubes = []
    for neighbor_cube_coordinate in _get_adjacent_coordinates(coordinate, dimension=dimension):
        if neighbor_cube_coordinate.tolist() in [c.tolist() for c in active_cubes]:
            adjacents_active_cubes.append(neighbor_cube_coordinate)
    return len(adjacents_active_cubes)


def apply_rule(active_cubes, dimension=3):
    new_active_cubes = []
    neighbors = list(np.unique(np.array(
        [cc for active_cube in active_cubes for cc in _get_adjacent_coordinates(active_cube, dimension=dimension)]
        ), axis=0))
    for cube in neighbors:
        nb_active_adjacents = _get_nb_adjacent_active(cube, active_cubes, dimension=dimension)
        if cube.tolist() in [c.tolist() for c in active_cubes]:
            if nb_active_adjacents in [2, 3]:
                new_active_cubes.append(cube)
        else:
            if nb_active_adjacents == 3:
                new_active_cubes.append(cube)
    return new_active_cubes


def run1(input_path):
    active_cubes = _parse(open(input_path).readlines())
    for _ in range(6):
        active_cubes = apply_rule(active_cubes)
    return len(active_cubes)


def run2(input_path):
    active_cubes = _parse(open(input_path).readlines(), dimension=4)
    for i in range(6):
        print("cycle %d" % i)
        active_cubes = apply_rule(active_cubes, dimension=4)
    return len(active_cubes)
    


if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
