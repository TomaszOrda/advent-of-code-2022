# from collections import deque

DECRYPTION_KEY = 811589153


class Decryptor:
    def __init__(self, lines) -> None:
        self.numbers = [int(line) for line in lines]
        self.id_0 = self.numbers.index(0)
        self.length = len(self.numbers)
        self.position_after_shifts = list(range(self.length))
        self.shifts = [number % (self.length - 1) for number in self.numbers]

    def apply_decryption_key(self, decryption_key):
        self.numbers = [number * decryption_key for number in self.numbers]
        self.shifts = [number % (self.length - 1) for number in self.numbers]

    def mix(self):
        for number_id in range(self.length):
            position = self.position_after_shifts[number_id]
            number = self.numbers[position]
            shift = self.shifts[number_id]
            del self.numbers[position]
            if shift + position < self.length:
                new_position = shift + position
                self.position_after_shifts = [
                    pos - 1 if pos in range(position, new_position + 1) else pos
                    for pos in self.position_after_shifts
                ]
            else:
                new_position = (shift + position) % (self.length - 1)
                self.position_after_shifts = [
                    pos + 1 if pos in range(new_position, position) else pos
                    for pos in self.position_after_shifts
                ]
            self.numbers.insert(new_position, number)
            self.position_after_shifts[number_id] = new_position


def solution(raw_input: str):
    encrypted_file = Decryptor(raw_input.splitlines())
    encrypted_file.apply_decryption_key(DECRYPTION_KEY)
    for _ in range(10):
        encrypted_file.mix()

    position_0 = encrypted_file.position_after_shifts[encrypted_file.id_0]
    position_0_1000 = (position_0 + 1000) % len(encrypted_file.numbers)
    position_0_2000 = (position_0 + 2000) % len(encrypted_file.numbers)
    position_0_3000 = (position_0 + 3000) % len(encrypted_file.numbers)
    groove_coordinates = sum((
        encrypted_file.numbers[position_0_1000],
        encrypted_file.numbers[position_0_2000],
        encrypted_file.numbers[position_0_3000]
    ))

    return groove_coordinates
