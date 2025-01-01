# with open('Day_7_test.txt') as f:
with open('Day_7.txt') as f:
    commands_executed = f.readlines()

directories = {}

sum_of_small_directories = 0

def find_size(index, directory):
    size = 0
    index+=2
    while(index<len(commands_executed) and not commands_executed[index].startswith("$ cd")):
        if commands_executed[index].startswith("dir"):
            size+=directories[commands_executed[index][4:-1]]
        else:
            size+=int(commands_executed[index].split()[0])
        index+=1
    directories[directory] = size
    if size<=100000:
        global sum_of_small_directories
        sum_of_small_directories+=size

for index, command in enumerate(reversed(commands_executed)):
    if command[0:4] == "$ cd" and not command == "$ cd ..\n":
        find_size(len(commands_executed)-1-index, command[5:-1])

print(sum_of_small_directories)