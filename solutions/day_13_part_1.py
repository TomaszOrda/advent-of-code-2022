import ast


# def find_closing_bracket(string, index):
#     opened_brackets = 1
#     while opened_brackets > 0:
#         index += 1
#         match string[index]:
#             case '[': opened_brackets += 1
#             case ']': opened_brackets -= 1
#     return index


# def parse_list(packet_str: str):
#     index = 1
#     while index < len(packet_str):
#         if packet_str[index] == ']' or packet_str[index] == ',':
#             index += 1
#         elif packet_str[index] == '[':
#             closing_bracket = find_closing_bracket(packet_str, index)
#             yield list(parse_list(packet_str[index:closing_bracket+1]))
#             index = closing_bracket
#         else:
#             next_comma = packet_str.find(",", index)
#             if next_comma != -1:
#                 yield int(packet_str[index:next_comma])
#                 index = next_comma
#             else:
#                 yield int(packet_str[index:-1])
#                 break

def is_in_right_order(x, y):
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

        if is_in_right_order(x[0], y[0]) == 'Equal':
            return is_in_right_order(x[1:], y[1:])
        else:
            return is_in_right_order(x[0], y[0])

    if isinstance(x, int):
        return is_in_right_order([x], y)
    if isinstance(y, int):
        return is_in_right_order(x, [y])


def solution(raw_input: str):
    # Note that one could simply use eval(). However it is not a good practice in general case.
    # packets = [eval(line) for line in raw_input.splitlines() if line != ""]
    # I did implement the parsing function, but there is an import for that
    # packets = [list(parse_list(line)) for line in raw_input.splitlines() if line != ""]
    packets = [ast.literal_eval(line) for line in raw_input.splitlines() if line != ""]
    pairs_of_packets = [packets[2*id:2*id+2] for id in range(len(packets)//2)]

    return sum(id+1 for (id, pair) in enumerate(pairs_of_packets) if is_in_right_order(*pair))
