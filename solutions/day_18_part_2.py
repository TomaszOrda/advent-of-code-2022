from enum import Enum
import numpy as np

PADDING = 3
# We need to reach each droplet
# And perhaps avoid confusion between the droplets on the sides of the grid


class Pocket(Enum):
    CUBE = 2
    AIR = 3
    EXPANSION = 1


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
    max_coordinate = cubes.max(axis=0) + PADDING

    sides = np.full(max_coordinate, 0)
    air = np.full(max_coordinate, Pocket.AIR)

    for cube in cubes:
        for adjacent in adjacent_to(cube, max_coordinate):
            sides[adjacent] += 1

    for cube in cubes:
        air[tuple(cube)] = Pocket.CUBE

    air_to_check = [tuple(max_coordinate - 1)]  # This coordinate is always outside of magma
    while len(air_to_check) > 0:
        coordinate = air_to_check.pop()
        air[coordinate] = Pocket.EXPANSION
        for adjacent in adjacent_to(coordinate, max_coordinate):
            if air[adjacent] == Pocket.AIR:
                air_to_check.append(adjacent)

    return sides[air == Pocket.EXPANSION].sum()
