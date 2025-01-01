# with open('Day_7_test.txt') as f:
with open('Day_7.txt') as f:
    commands_executed = f.readlines()

directories = {}

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

for index, command in enumerate(reversed(commands_executed)):
    if command[0:4] == "$ cd" and not command == "$ cd ..\n":
        find_size(len(commands_executed)-1-index, command[5:-1])

space_needed=30000000-(70000000-directories["/"])
# print(space_needed)

directories = {}
last_candidate_size = 70000000

def find_candidate(index, directory):
    size = 0
    index+=2
    while(index<len(commands_executed) and not commands_executed[index].startswith("$ cd")):
        if commands_executed[index].startswith("dir"):
            size+=directories[commands_executed[index][4:-1]]
        else:
            size+=int(commands_executed[index].split()[0])
        index+=1
    directories[directory] = size
    global last_candidate_size
    if size<last_candidate_size and size>=space_needed: 
        last_candidate_size = size 
    

for index, command in enumerate(reversed(commands_executed)):
    if command[0:4] == "$ cd" and not command == "$ cd ..\n":
        find_candidate(len(commands_executed)-1-index, command[5:-1])

print(last_candidate_size)