def shared_item(backpack: str):
    middle = len(backpack)//2
    compartment_1 = backpack[:middle]
    compartment_2 = backpack[middle:]
    return set(compartment_1).intersection(set(compartment_2)).pop()

def priority(item: str):
    order = ord(item)
    # Capital letters have smaller order than lowercase
    if order < ord('a'):
        return order - ord('A') + 27
    else:
        return order - ord('a') + 1


def solution(raw_input: str):
    backpacks = raw_input.splitlines()
    return sum(
        [priority(shared_item(backpack))for backpack in backpacks]
    )
