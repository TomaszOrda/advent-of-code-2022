def elf_backpacks(calories_list):
    backpack = 0
    for line in calories_list:
        if line == "":
            yield backpack
            backpack = 0
        else:
            backpack += int(line)


def solution(raw_input: str):
    calories_list = raw_input.splitlines()
    return max(elf_backpacks(calories_list))
