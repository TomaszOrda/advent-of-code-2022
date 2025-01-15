import numpy as np


def adjacent_to(cube, max_coordinate):
    return [((cube[0] + x) % max_coordinate[0],
            (cube[1] + y) % max_coordinate[1],
            (cube[2] + z) % max_coordinate[2])
            for (x, y, z) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
            ]


def solution(raw_input: str):
    cubes = np.array([
        tuple(int(coordinate) for coordinate in line.split(',')) for line in raw_input.splitlines()
    ])
    max_coordinate = cubes.max(axis=0) + 1

    sides = np.full(max_coordinate, 0)

    for cube in cubes:
        for adjacent in adjacent_to(cube, max_coordinate):
            sides[adjacent] += 1

    for cube in cubes:
        sides[tuple(cube)] = 0

    return sides.sum()
