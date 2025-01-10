from dataclasses import dataclass

STACK_SPACING = 4


@dataclass
class Command:
    amount: int
    from_stack: int
    to_stack: int


class Ship:
    def __init__(self, input_lines: list[str]) -> None:
        levels = [line[1::STACK_SPACING] for line in reversed(input_lines)]
        self.stacks = [list(stack) for stack in zip(*levels)]
        for stack_id, _ in enumerate(self.stacks):
            self.stacks[stack_id] = [crate for crate in self.stacks[stack_id][1:] if crate != " "]

    def exec(self, command: Command) -> None:
        crates = self.stacks[command.from_stack-1][-command.amount:]
        self.stacks[command.from_stack-1] = self.stacks[command.from_stack-1][:-command.amount]
        self.stacks[command.to_stack-1].extend(crates)

    def top_crates(self) -> str:
        return ''.join((stack[-1] for stack in self.stacks))


def solution(raw_input: str) -> str:
    lines = raw_input.splitlines()
    split_point = lines.index("")

    ship = Ship(lines[:split_point])
    commands = [Command(*(int(x) for x in line.split(" ")[1::2])) for line in lines[split_point+1:]]

    for command in commands:
        ship.exec(command)

    return ship.top_crates()
