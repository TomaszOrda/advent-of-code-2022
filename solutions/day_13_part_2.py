import ast


# The recursive function is not the pretties here, because of all the equal cases
# But it does allow me to resule a lot of logic
# And the recursive code has its strengths in simplicity
def packet_less_than(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x == y:
            return 'Equal'
        return x < y
    if isinstance(x, list) and isinstance(y, list):
        if len(x) == 0 and len(y) > 0:
            return True
        if len(x) > 0 and len(y) == 0:
            return False
        if len(x) == 0 and len(y) == 0:
            return 'Equal'

        if packet_less_than(x[0], y[0]) == 'Equal':
            return packet_less_than(x[1:], y[1:])
        else:
            return packet_less_than(x[0], y[0])

    if isinstance(x, int):
        return packet_less_than([x], y)
    if isinstance(y, int):
        return packet_less_than(x, [y])


class Packet:
    def __init__(self, string_representation) -> None:
        self.values = ast.literal_eval(string_representation)

    def __lt__(self, other):
        return packet_less_than(self.values, other.values) is True

    def __eq__(self, other):
        return packet_less_than(self.values, other.values) == 'Equal'


def solution(raw_input: str):
    packets = [Packet(line) for line in raw_input.splitlines() if line != ""]

    divider_packet_2 = Packet("[[2]]")
    divider_packet_6 = Packet("[[6]]")
    packets.extend([divider_packet_2, divider_packet_6])

    packets.sort()

    return (packets.index(divider_packet_2) + 1) * (packets.index(divider_packet_6) + 1)
