import re


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
        self.grid = [[]] + [' ' + line + ' ' for line in lines] + [[]]
        self.facing = [0, 1]
        self.position = [1, self.grid[1].index('.')]

    def within_the_map(self, pos):
        return len(self.grid[pos[0]]) > pos[1] >= 0 and self.grid[pos[0]][pos[1]] != ' '

    def next_tile(self):
        next_position = [self.position[0]+self.facing[0], self.position[1]+self.facing[1]]
        if not self.within_the_map(next_position):
            while self.within_the_map([next_position[0]-self.facing[0], next_position[1]-self.facing[1]]):
                next_position[0] -= self.facing[0]
                next_position[1] -= self.facing[1]
        return next_position

    def exec(self, command: Command) -> None:
        if command.forward:
            for _ in range(command.forward):
                next_position = self.next_tile()
                if self.grid[next_position[0]][next_position[1]] == '#':
                    break
                self.position = next_position
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
