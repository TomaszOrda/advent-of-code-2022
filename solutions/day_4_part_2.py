def parse_assignment(assignment: str):
    elves = assignment.split(",")
    return tuple(
        tuple(map(int, elf.split("-")))
        for elf in elves
    )

def overlaps(pair):
    elf_1 = set(range(pair[0][0], pair[0][1]+1))
    elf_2 = set(range(pair[1][0], pair[1][1]+1))
    return len(elf_1.intersection(elf_2)) != 0

# More efficient code, however much more verbose
# def fully_contains(pair):
#     elf_1 = pair[0]
#     elf_2 = pair[1]
#     return (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or \
#            (elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1])

# def overlaps(pair):
#     elf_1 = pair[0]
#     elf_2 = pair[1]
#     return fully_contains(pair) or elf_2[0] <= elf_1[0] <= elf_2[1] or elf_2[0] <= elf_1[1] <= elf_2[1]


def solution(raw_input: str):
    pairs = [parse_assignment(assignment) for assignment in raw_input.splitlines()]
    return sum(1 for pair in pairs if overlaps(pair))
