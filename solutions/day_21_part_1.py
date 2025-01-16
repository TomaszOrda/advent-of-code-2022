OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}


class MonkeyVariable:
    def __init__(self, value: str) -> None:
        if value.isnumeric():
            self.constant = True
            self.value = int(value)
        else:
            self.constant = False
            equation = value.split(" ")
            self.left = equation[0]
            self.operator = equation[1]
            self.right = equation[2]


class MonkeyCalculator:
    def __init__(self, monkeys: list[str]) -> None:
        self.monkey_instructions: dict[str, MonkeyVariable] = {}
        for monkey in monkeys:
            monkey_id = monkey.split(': ')[0]
            equation = monkey.split(': ')[1]
            self.monkey_instructions[monkey_id] = MonkeyVariable(equation)

    def evaluate(self, monkey_id):
        monkey = self.monkey_instructions[monkey_id]
        if monkey.constant:
            return monkey.value
        else:
            left = self.evaluate(monkey.left)
            right = self.evaluate(monkey.right)
            result = OPERATORS[monkey.operator](left, right)
            self.monkey_instructions[monkey_id] = MonkeyVariable(str(result))
            return result


def solution(raw_input: str):
    monkey_calculator = MonkeyCalculator(raw_input.splitlines())
    return monkey_calculator.evaluate("root")
