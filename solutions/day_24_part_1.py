import numpy as np

DIRECTIONS = ['^', '>', '<', 'v']
ROLL_SHIFT_AXIS = {
    '^': (-1, 0),
    '>': (1, 1),
    '<': (-1, 1),
    'v': (1, 0),
}


class Valley:
    def __init__(self, lines) -> None:
        grid_shape = (len(lines), len(lines[0]))
        self.blizzards = {
            blizzard_type: np.full(grid_shape, False)
            for blizzard_type in DIRECTIONS
        }
        self.walls = np.full(grid_shape, False)

        for y, line in enumerate(lines):
            for x, tile in enumerate(line):
                if tile == "#":
                    self.walls[y, x] = True
                elif tile == ".":
                    continue
                else:
                    self.blizzards[tile][y, x] = True

        self.entry = (0, 1)
        self.exit = (grid_shape[0] - 1, grid_shape[1] - 2)

        self.reachable = set([self.entry])
        self.time_taken = 0

    def simulate(self):
        for direction, blizzard in self.blizzards.items():
            shift, axis = ROLL_SHIFT_AXIS[direction]
            self.blizzards[direction] = np.roll(blizzard, shift, axis)

        self.blizzards["<"][:, -2] = self.blizzards["<"][:, 0]
        self.blizzards[">"][:, 1] = self.blizzards[">"][:, -1]
        self.blizzards["^"][-2] = self.blizzards["^"][0]
        self.blizzards["v"][1] = self.blizzards["v"][-1]
        # We do not really need to remove the blizzard that are in the walls
        # as they are going to be overwritten anyway

    def is_in_blizzard(self, pos):
        y, x = pos
        return any(
            blizzard[y, x]
            for blizzard in self.blizzards.values()
        )

    def neighbours(self, pos):
        if pos == self.entry:
            return [self.entry, (self.entry[0] + 1, self.entry[1])]
        if pos == self.exit:
            return [self.exit, (self.exit[0] - 1, self.entry[1])]
        y, x = pos
        return [
            (y + d[0], x + d[1])
            for d in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]
        ]

    def find_path(self):
        while self.exit not in self.reachable:
            self.simulate()
            self.reachable = set(
                neighbour
                for pos in self.reachable
                for neighbour in self.neighbours(pos)
                if not self.is_in_blizzard(neighbour)
                if not self.walls[neighbour]
            )
            self.time_taken += 1


def solution(raw_input: str):
    valley = Valley(raw_input.splitlines())
    valley.find_path()
    return valley.time_taken
