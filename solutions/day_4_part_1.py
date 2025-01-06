def parse_assignment(assignment: str):
    elves = assignment.split(",")
    return tuple(
        tuple(map(int, elf.split("-")))
        for elf in elves
    )

def fully_contains(pair):
    elf_1 = pair[0]
    elf_2 = pair[1]
    return (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or \
           (elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1])


def solution(raw_input: str):
    pairs = [parse_assignment(assignment) for assignment in raw_input.splitlines()]
    return sum(1 for pair in pairs if fully_contains(pair))
