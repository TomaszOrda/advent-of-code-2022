import re
import numpy as np
# The solution is not net agnostic — it works for test case and for the kind of net I got.


class Command:
    def __init__(self, comm: str) -> None:
        self.forward = None
        self.turn = None
        if comm.isnumeric():
            self.forward = int(comm)
        else:
            self.turn = comm


class Map:
    def __init__(self, lines: list[str]) -> None:
        self.grid_shape = (len(lines) + 2, max(len(line)+2 for line in lines))
        self.grid = np.full(self.grid_shape, " ")
        for row, line in enumerate(lines):
            for col, tile in enumerate(line):
                self.grid[row + 1, col + 1] = tile

        self.cube_width = min(
            1 + max(line.rfind("."), str(line).rfind("#")) - min(line.find("."), line.find("#"))
            for line in lines
        )
        self.position = [1, lines[0].find('.') + 1]
        self.facing = [0, 1]
        w = self.cube_width
        self.portals = {}
        if self.cube_width == 4:  # Test case
            self.add_portal(lambda d: ((0, 9+d), (-1, 0)), lambda d: ((4, 4 - d), (1, 0)))
            self.add_portal(lambda d: ((1 + d, 8), (0, 1)), lambda d: ((4, 5 + d), (1, 0)))
            self.add_portal(lambda d: ((1 + d, 13), (0, -1)), lambda d: ((12 - d, 18), (0, -1)))
            self.add_portal(lambda d: ((5 + d, 0), (0, 1)), lambda d: ((13, 16-d), (0, -1)))
            self.add_portal(lambda d: ((5 + d, 13), (0, -1)), lambda d: ((8, 16-d), (1, 0)))
            self.add_portal(lambda d: ((9, 1+d), (-1, 0)), lambda d: ((13, 12-d), (-1, 0)))
            self.add_portal(lambda d: ((9, 5+d), (-1, 0)), lambda d: ((12-d, 8), (1, 0)))
        else:  # Input (It does work only for one type of net. I suppose there is 10 more different nets)
            self.add_portal(lambda d: ((0, 1+w + d), (1, 0)), lambda d: ((1+3*w + d, 0), (0, 1)))
            self.add_portal(lambda d: ((0, 1+2*w + d), (1, 0)), lambda d: ((1+4*w, 1 + d), (-1, 0)))
            self.add_portal(lambda d: ((1 + d, 1+3*w), (0, -1)), lambda d: ((3*w - d, 2*w+1), (0, -1)))
            self.add_portal(lambda d: ((1 + d, w), (0, 1)), lambda d: ((3*w - d, 0), (0, 1)))
            self.add_portal(lambda d: ((1 + w, 1 + 2*w + d), (-1, 0)), lambda d: ((1 + w + d, 1+2*w), (0, -1)))
            self.add_portal(lambda d: ((1 + w + d, w), (0, 1)), lambda d: ((2*w, 1 + d), (1, 0)))
            self.add_portal(lambda d: ((1 + 3*w, 1 + w + d), (-1, 0)), lambda d: ((1 + 3*w + d, 1+w), (0, -1)))

    def add_portal(self, entry, out):
        for offset in range(self.cube_width + 1):
            self.portals[entry(offset)] = out(offset)
            self.portals[out(offset)] = entry(offset)

    def within_the_map(self, pos):
        return self.grid[pos] != ' '

    def next_tile(self):
        next_position = [self.position[0]+self.facing[0], self.position[1]+self.facing[1]]
        next_facing = self.facing
        if not self.within_the_map(tuple(next_position)):
            next_position, next_facing = self.portals[tuple(next_position), (-next_facing[0], -next_facing[1])]
            next_position = [next_position[0]+next_facing[0], next_position[1]+next_facing[1]]
        return next_position, next_facing

    def exec(self, command: Command) -> None:
        if command.forward:
            for _ in range(command.forward):
                next_position, next_facing = self.next_tile()
                if self.grid[next_position[0]][next_position[1]] == '#':
                    break
                self.position = next_position
                self.facing = next_facing
        else:
            if command.turn == "R":
                self.facing = [self.facing[1], -self.facing[0]]
            else:
                self.facing = [-self.facing[1], self.facing[0]]

    def current_password(self):
        match self.facing:
            case([0, 1]): facing_value = 0
            case([1, 0]): facing_value = 1
            case([0, -1]): facing_value = 2
            case(_): facing_value = 3
        return 1000 * self.position[0] + 4 * self.position[1] + facing_value


def solution(raw_input: str):
    jungle_map = Map(raw_input.splitlines()[:-2])
    commands = [Command(comm) for comm in re.split(r'(\d+)', raw_input.splitlines()[-1])][1:-1]

    for command in commands:
        jungle_map.exec(command)

    return jungle_map.current_password()
