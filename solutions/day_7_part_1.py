def solution(raw_input: str):
    commands_executed = raw_input.splitlines()
    directories = {}

    def find_size(index, directory):
        size = 0
        for command in commands_executed[index+2:]:
            if command.startswith("$ cd"):
                break
            if command.startswith("dir"):
                size += directories[command[4:]]
            else:
                size += int(command.split()[0])

        directories[directory] = size
        if size<=100000:
            return size
        else:
            return 0

    size_of_small_directories = [
        find_size(len(commands_executed)-1-index, command[5:])
        for index, command in enumerate(reversed(commands_executed))
        if command[0:4] == "$ cd" and not command == "$ cd .."
    ]

    return sum(size_of_small_directories)
