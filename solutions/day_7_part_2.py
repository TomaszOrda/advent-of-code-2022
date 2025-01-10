def solution(raw_input: str):
    commands_executed = raw_input.splitlines()
    directories = {}

    def find_size(index):
        size = 0
        for command in commands_executed[index+2:]:
            if command.startswith("$ cd"):
                break
            if command.startswith("dir"):
                size += directories[command[4:]]
            else:
                size += int(command.split()[0])
        return size

    for index, command in enumerate(reversed(commands_executed)):
        if command.startswith("$ cd") and not command.endswith(".."):
            directory = command[5:]
            directories[directory] = find_size(len(commands_executed)-1-index)

    space_needed = 30000000-(70000000-directories["/"])

    smallest_candidate_size = min(dir_size for dir_size in directories.values() if dir_size >= space_needed)

    return smallest_candidate_size
