OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}
REVERSE = {
    "+": "-",
    "-": "+",
    "*": "/",
    "/": "*"
}


class MonkeyVariable:
    def __init__(self, value: str | tuple | int) -> None:
        self.constant = False
        self.variable = False
        self.human = False
        self.expression = False
        if isinstance(value, tuple):
            self.expression = True
            self.operator, self.left, self.right = value
        elif isinstance(value, int):
            self.constant = True
            self.value = value
        elif value == "humn":
            self.human = True
        elif value.isnumeric():
            self.constant = True
            self.value = int(value)
        elif " " in value:
            self.expression = True
            equation = value.split(" ")
            self.operator = equation[1]
            self.left = MonkeyVariable(equation[0])
            self.right = MonkeyVariable(equation[2])
        else:
            self.variable = True
            self.monkey_id = value


class MonkeyCalculator:
    def __init__(self, monkeys: list[str]) -> None:
        self.monkey_instructions: dict[str, MonkeyVariable] = {}
        for monkey in monkeys:
            monkey_id = monkey.split(': ')[0]
            equation = monkey.split(': ')[1]
            self.monkey_instructions[monkey_id] = MonkeyVariable(equation)

    def evaluate(self, monkey: MonkeyVariable) -> MonkeyVariable:
        if monkey.variable:
            return self.evaluate(self.monkey_instructions[monkey.monkey_id])
        if monkey.human or monkey.constant:
            return monkey

        # It makes everything much easier to assume that each monkey is used only once
        # That fact is kind of implied in text
        # Because of that caching in unnecessary
        left = self.evaluate(monkey.left)
        right = self.evaluate(monkey.right)
        if left.constant and right.constant:
            result = OPERATORS[monkey.operator](left.value, right.value)
            # self.monkey_instructions[monkey_id] = MonkeyVariable(str(result))
        else:
            result = (monkey.operator, left, right)
            # self.monkey_instructions[monkey_id] = MonkeyVariable(result)
        return MonkeyVariable(result)

    def find_humn_value(self):
        left = self.monkey_instructions["root"].left
        right = self.monkey_instructions["root"].right
        left = self.evaluate(left)
        right = self.evaluate(right)
        if right.constant:
            return self.find_humn_value_aux(left, right)
        else:
            return self.find_humn_value_aux(right, left)

    def find_humn_value_aux(self, expression: MonkeyVariable, constant: MonkeyVariable):
        if expression.human:
            return constant.value
        operator = expression.operator
        left = expression.left
        right = expression.right
        if left.constant:
            inner_constant = left
            inner_expression = right
        else:
            inner_constant = right
            inner_expression = left
        if operator in ["+", "*"]:
            return self.find_humn_value_aux(
                inner_expression,
                self.evaluate(MonkeyVariable((REVERSE[operator], constant, inner_constant))))
        else:
            if left.constant:
                return self.find_humn_value_aux(
                    inner_expression,
                    self.evaluate(MonkeyVariable((operator, inner_constant, constant))))
            else:
                return self.find_humn_value_aux(
                    inner_expression,
                    self.evaluate(MonkeyVariable((REVERSE[operator], inner_constant, constant))))


def solution(raw_input: str):
    monkey_calculator = MonkeyCalculator(raw_input.splitlines())
    return monkey_calculator.find_humn_value()
