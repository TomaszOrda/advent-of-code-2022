from math import ceil, prod, lcm
from typing import Tuple


class Monkey:
    def __init__(self, lines: list[str]) -> None:
        self.id = lines[0].split()[-1].split(":")[0]
        self.activity = 0
        self.items = [int(worry_level) for worry_level in lines[1].split(":")[-1].split(", ")]
        operation_text = lines[2].split(" = ")[-1].split()
        left = (lambda x: x) if operation_text[0] == 'old' else lambda _: int(operation_text[0])
        right = (lambda x: x) if operation_text[2] == 'old' else lambda _: int(operation_text[2])
        operator = (lambda x, y: x * y) if operation_text[1] == "*" else (lambda x, y: x + y)
        self.operation = {'left': left, 'operator': operator, 'right': right}
        self.test = int(lines[3].split()[-1])
        self.throw_to = {
            True: int(lines[4].split()[-1]),
            False: int(lines[5].split()[-1])
        }

    def recalculate_worry_level(self, worry_level):
        left = self.operation['left'](worry_level)
        right = self.operation['right'](worry_level)
        return self.operation['operator'](left, right)//3

    def inspect(self, worry_level: int) -> Tuple[int, int]:
        new_worry_level = self.recalculate_worry_level(worry_level)
        throw_to = self.throw_to[new_worry_level % self.test == 0]
        self.activity += 1
        return (throw_to, new_worry_level)

    def take_turn(self) -> list[Tuple[int, int]]:
        result = [self.inspect(worry_level) for worry_level in self.items]
        self.items = []
        return result


def solution(raw_input: str):
    lines = raw_input.splitlines()
    monkeys = [Monkey(lines[i*7:(i+1)*7]) for i in range(ceil(len(lines)/7))]

    monkeys_test_lcm = lcm(*(monkey.test for monkey in monkeys))

    for _ in range(20):
        for monkey in monkeys:
            thrown_items = monkey.take_turn()
            for (throw_to, item) in thrown_items:
                monkeys[throw_to].items.append(item % monkeys_test_lcm)

    return prod(sorted([monkey.activity for monkey in monkeys])[-2:])
