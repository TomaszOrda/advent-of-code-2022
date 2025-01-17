from collections import deque


class Crater:
    def __init__(self, lines: list[str]) -> None:
        self.elves: set[tuple[int, int]] = set(
            (x, y)
            for (y, line) in enumerate(lines)
            for (x, tile) in enumerate(line)
            if tile == "#"
        )
        self.directions: deque[list[tuple[int, int]]] = deque([
            [(0, -1), (1, -1), (-1, -1)],
            [(0, 1), (1, 1), (-1, 1)],
            [(-1, 0), (-1, -1), (-1, 1)],
            [(1, 0), (1, -1), (1, 1)],
        ])

    def has_space(self, elf) -> bool:
        x, y = elf
        return all(
            (x+dx, y+dy) not in self.elves
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if (dx, dy) != (0, 0)
        )

    def action(self, elf) -> tuple[int, int]:
        x, y = elf
        if self.has_space(elf):
            return elf
        for direction in self.directions:
            if all((x+tile[0], y+tile[1]) not in self.elves for tile in direction):
                return (x + direction[0][0], y+direction[0][1])
        return elf

    def simulate_round(self):
        move_requests: dict[tuple[int, int], list[tuple[int, int]]] = {}
        for elf in self.elves:
            requested_move = self.action(elf)
            move_requests.setdefault(requested_move, []).append(elf)

        for requested_move, elves in move_requests.items():
            if len(elves) == 1:
                elf = elves.pop()
                self.elves.remove(elf)
                self.elves.add(requested_move)

        self.directions.rotate(-1)

    def empty_tiles_in_the_rectangle(self):
        x_coords, y_coords = zip(*self.elves)
        x_max, y_max = max(x_coords), max(y_coords)
        x_min, y_min = min(x_coords), min(y_coords)
        return (y_max - y_min + 1) * (x_max - x_min + 1) - len(self.elves)


def solution(raw_input: str):
    crater = Crater(raw_input.splitlines())

    for _ in range(10):
        crater.simulate_round()

    return crater.empty_tiles_in_the_rectangle()
