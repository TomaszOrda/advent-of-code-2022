from itertools import cycle, islice
import numpy as np

ROCKS_TO_FALL = 2022
DIRECTION = {'<': -1, '>': 1}
ROCK_TYPES = [
        [list("####")],

        [list(".#."), list("###"), list(".#.")],

        [list("###"), list("..#"), list("..#")],

        [list("#"), list("#"), list("#"), list("#")],

        [list("##"), list("##")]
    ]


class Cave:
    def __init__(self, jets) -> None:
        self.chamber = np.full((ROCKS_TO_FALL*4, 9), '.')
        self.chamber[0, :], self.chamber[:, 0], self.chamber[:, -1] = '-', '|', '|'
        self.chamber[0, 0], self.chamber[0, -1] = '+', '+'
        self.top_rock = 0
        self.jets = cycle(jets)

    def start_position(self):
        return [self.top_rock + 4, 3]

    def collide(self, position, rock_type):
        for rock_y, line in enumerate(rock_type):
            for rock_x, rock_field in enumerate(line):
                if self.chamber[position[0]+rock_y, position[1] + rock_x] != '.' and rock_field == "#":
                    return True
        return False

    def add_rock(self, position, rock_type):
        for rock_y, line in enumerate(rock_type):
            for rock_x, field in enumerate(line):
                if field == "#":
                    self.chamber[position[0]+rock_y, position[1]+rock_x] = '#'

    def simulate_rocks(self):
        for rock_type in islice(cycle(ROCK_TYPES), ROCKS_TO_FALL):
            rock_position = self.start_position()
            for jet in self.jets:
                if not self.collide([rock_position[0], rock_position[1] + DIRECTION[jet]], rock_type):
                    rock_position[1] += DIRECTION[jet]
                if not self.collide([rock_position[0]-1, rock_position[1]], rock_type):
                    rock_position[0] -= 1
                else:
                    self.add_rock(rock_position, rock_type)
                    self.top_rock = max(self.top_rock, rock_position[0]+len(rock_type)-1)
                    break


def solution(raw_input: str):
    jets = raw_input.rstrip()
    cave = Cave(jets)
    cave.simulate_rocks()

    return cave.top_rock
