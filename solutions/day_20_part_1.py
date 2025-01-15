def solution(raw_input: str):

    numbers = [{'value': int(line), 'visited': False} for line in raw_input.splitlines()]

    for _ in range(len(numbers)):
        while numbers[0]['visited']:
            numbers.append(numbers[0])
            del numbers[0]
        numbers[0]['visited'] = True
        number_holder = numbers[0]
        del numbers[0]
        numbers.insert(
            number_holder['value'] % len(numbers),
            number_holder)

    id_zero = numbers.index({'value': 0, 'visited': True})
    number_1000th = numbers[(id_zero+1000) % len(numbers)]['value']
    number_2000th = numbers[(id_zero+2000) % len(numbers)]['value']
    number_3000th = numbers[(id_zero+3000) % len(numbers)]['value']

    return number_1000th + number_2000th + number_3000th
