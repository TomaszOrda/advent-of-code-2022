DURATION = {"noop": 1, "addx": 2}


def solution(raw_input: str):
    instructions = [
        dict(zip(['type', 'value'], line.split()))
        for line in raw_input.splitlines()
    ]

    clock = 0
    memory = 1
    signal_strength = 0

    for instruction in instructions:
        for _ in range(DURATION[instruction['type']]):
            clock += 1
            if clock % 40 == 20:
                signal_strength += memory*clock
        if instruction['type'] == 'addx':
            memory += int(instruction['value'])

    return signal_strength
