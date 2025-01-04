def elf_backpacks(calories_list):
    backpack = 0
    for line in calories_list:
        if line == "":
            yield backpack
            backpack = 0
        else:
            backpack += int(line)
    yield backpack


def solution(raw_input: str):
    calories_list = raw_input.splitlines()
    # A custom max function would be asymptotically faster
    return sum(sorted(list(elf_backpacks(calories_list)))[-3:])
