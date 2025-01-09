DURATION = {"noop": 1, "addx": 2}


def sprite_visible(signal, clock):
    horizontal_position_clock = clock % 40
    horizontal_position_sprite = signal + 1
    return (horizontal_position_clock - horizontal_position_sprite) % 40 in [-1 % 40, 0, 1]


def solution(raw_input: str):
    instructions = [
        dict(zip(['type', 'value'], line.split()))
        for line in raw_input.splitlines()
    ]

    clock = 0
    memory = 1
    image = ""

    for instruction in instructions:
        for _ in range(DURATION[instruction['type']]):
            clock += 1
            if sprite_visible(memory, clock):
                image += "#"
            else:
                image += "."
            if clock % 40 == 0:
                image += "\n"
        if instruction['type'] == 'addx':
            memory += int(instruction['value'])

    image = image.rstrip()
    return image
