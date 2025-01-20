DECRYPTION_KEY = 811589153


class Decryptor:
    def __init__(self, lines) -> None:
        self.numbers = [int(line) for line in lines]
        self.id_0 = self.numbers.index(0)
        self.length = len(self.numbers)
        self.id_to_position = list(range(self.length))
        self.position_to_id = list(range(self.length))
        self.shifts = [number % (self.length - 1) for number in self.numbers]

    def apply_decryption_key(self, decryption_key):
        self.numbers = [number * decryption_key for number in self.numbers]
        self.shifts = [number % (self.length - 1) for number in self.numbers]

    def mix(self):
        for number_id, position in enumerate(self.id_to_position):
            shift = self.shifts[number_id]

            if shift + position < self.length:
                new_position = shift + position
                for pos in range(position, new_position):
                    right_neighbour = self.position_to_id[pos + 1]
                    self.id_to_position[right_neighbour] -= 1
                    self.position_to_id[pos] = right_neighbour
            else:
                new_position = (shift + position + 1) % self.length
                for pos in range(position, new_position, -1):
                    left_neighbour = self.position_to_id[pos - 1]
                    self.id_to_position[left_neighbour] += 1
                    self.position_to_id[pos] = left_neighbour

            self.id_to_position[number_id] = new_position
            self.position_to_id[new_position] = number_id


def solution(raw_input: str):
    encrypted_file = Decryptor(raw_input.splitlines())
    encrypted_file.apply_decryption_key(DECRYPTION_KEY)
    for _ in range(10):
        encrypted_file.mix()

    position_0 = encrypted_file.id_to_position[encrypted_file.id_0]

    groove_coordinates = 0
    for shift in [1000, 2000, 3000]:

        position = (position_0 + shift) % encrypted_file.length
        number_id = encrypted_file.position_to_id[position]
        groove_coordinates += encrypted_file.numbers[number_id]

    return groove_coordinates
