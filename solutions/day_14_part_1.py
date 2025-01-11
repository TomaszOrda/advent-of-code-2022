import numpy as np


class Cave:
    def __init__(self, scan) -> None:
        x_coords = [x for line in scan for (x, _) in line]
        y_coords = [y for line in scan for (_, y) in line]
        self.right = max(x_coords) + 1
        self.left = min(x_coords) - 1
        self.down = max(y_coords) + 3
        self.top = 0
        self.cave = np.full((self.down, self.right - self.left + 1 + 2), '.')
        self.inlet = (0, 500 - self.left + 1)
        self.pieces_of_sand_fallen = 0
        for line in scan:
            for index in range(0, len(line)-1):
                start, end = line[index:index + 2]
                self.cave[
                    min(start[1], end[1]):max(start[1], end[1])+1,
                    min(start[0], end[0])-self.left+1:max(start[0], end[0])-self.left+2] = '#'

    def simulate_sand_falling(self):
        sand = self.inlet
        while True:
            if sand[0] == self.down - 1:
                # self.display()
                break
            drop_place = self.drop(sand)
            if sand == drop_place:
                self.cave[sand] = 'o'
                sand = self.inlet
                self.pieces_of_sand_fallen += 1
            else:
                sand = drop_place

    def drop(self, sand):
        y, x = sand
        below = [(y+1, x), (y+1, x-1), (y+1, x+1), (y, x)]
        return [space for space in below if self.cave[space[0], space[1]] == '.'][0]

    def display(self):
        np.set_printoptions(threshold=512)
        np.set_printoptions(linewidth=128)
        print(self.cave)


def solution(raw_input: str):
    scan = [
        [tuple(map(int, coords.split(','))) for coords in line.strip().split(' -> ')]
        for line in raw_input.splitlines()
    ]
    cave = Cave(scan)
    cave.simulate_sand_falling()
    return cave.pieces_of_sand_fallen
