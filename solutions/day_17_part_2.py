from itertools import cycle, islice
from math import ceil
import numpy as np

ROCKS_TO_FALL = 1_000_000_000_000
DIRECTION = {'<': -1, '>': 1}
ROCK_TYPES = [
        np.array([[True, True, True, True]]),  # Horizontal line
        np.array([[False, True, False], [True, True, True], [False, True, False]]),  # Cross
        np.array([[True, True, True], [False, False, True], [False, False, True]]),  # L
        np.array([[True], [True], [True], [True]]),  # Vertical line
        np.array([[True, True], [True, True]])  # Square
]


class Cave:
    def __init__(self, jets) -> None:
        self.chamber = np.full((ROCKS_TO_FALL // 100_000_000, 9), False)
        self.chamber[0, :] = self.chamber[:, 0] = self.chamber[:, -1] = True
        self.top_rock = 0
        self.jets = cycle(enumerate(jets))
        self.rocks = islice(cycle(enumerate(ROCK_TYPES)), ROCKS_TO_FALL)
        self.cache = []
        self.top_rock_positions = []

    def cycle_detected_at(self, cycle_check_depth):
        # if len(self.cache) < 2 * cycle_check_depth:
        #     return False
        # Make sure that the cycle_start points at the same rock type as the last rock
        cycle_start = ceil(len(self.cache)/2) + (ceil(len(self.cache)/2) - len(self.cache)) % len(ROCK_TYPES)
        for cycle_start_index in range(cycle_start, len(self.cache) - cycle_check_depth + 1, len(ROCK_TYPES)):
            if all(
                    formation_1 == formation_2
                    for formation_1, formation_2
                    in zip(
                        self.cache[-cycle_check_depth:],
                        self.cache[cycle_start_index-cycle_check_depth:cycle_start_index])
                    ):
                return cycle_start_index
        return False

    def start_position(self):
        return [self.top_rock + 4, 3]

    def collides(self, position, rock):
        y, x = position
        h, w = rock.shape
        return np.any(self.chamber[y:y+h, x:x+w] & rock)

    def add_rock(self, position, rock):
        y, x = position
        h, w = rock.shape
        self.chamber[y:y+h, x:x+w] |= rock

    def cache_rock(self, rock_position, rock_id, jet_id):
        self.cache.append(
            (rock_position[1], rock_id, jet_id)
        )

    def tower_height(self, cycle_check_depth):
        # This only works when there is a cycle. For small amount of rocks to fall go back to part 1
        while not (cycle_start_index := self.cycle_detected_at(cycle_check_depth)):
            self.simulate_rock_falling()
        return self.tower_height_skip_cycles(
            cycle_start_index=cycle_start_index,
            cycle_length=len(self.cache) - cycle_start_index)

    def simulate_rock_falling(self):
        rock_id, rock_type = next(self.rocks)
        rock_position = self.start_position()
        for jet_id, jet in self.jets:
            if not self.collides([rock_position[0], rock_position[1] + DIRECTION[jet]], rock_type):
                rock_position[1] += DIRECTION[jet]
            if not self.collides([rock_position[0]-1, rock_position[1]], rock_type):
                rock_position[0] -= 1
            else:
                self.add_rock(rock_position, rock_type)
                self.cache_rock(rock_position, rock_id, jet_id)

                self.top_rock = max(self.top_rock, rock_position[0]+len(rock_type)-1)
                self.top_rock_positions.append(self.top_rock)
                break

    def tower_height_skip_cycles(self, cycle_start_index, cycle_length):
        cycle_height = (self.top_rock_positions[cycle_start_index + cycle_length - 1] -
                        self.top_rock_positions[cycle_start_index - 1])

        base_rocks = cycle_start_index - cycle_length
        remaining_rocks = ROCKS_TO_FALL - base_rocks
        tip_rocks = remaining_rocks % cycle_length

        cycle_count = remaining_rocks // cycle_length
        if base_rocks + tip_rocks == 0:
            base_and_tip_height = 0
        else:
            base_and_tip_height = self.top_rock_positions[base_rocks + tip_rocks - 1]

        return cycle_count * cycle_height + base_and_tip_height


def solution(raw_input: str):
    jets = raw_input.rstrip()
    cave = Cave(jets)
    return cave.tower_height(cycle_check_depth=20)
