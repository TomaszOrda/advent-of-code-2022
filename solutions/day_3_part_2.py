def shared_item(group: list[str]):
    return set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()


def priority(item: str):
    order = ord(item)
    # Capital letters have smaller order than lowercase
    if order < ord('a'):
        return order - ord('A') + 27
    else:
        return order - ord('a') + 1


def solution(raw_input: str):
    backpacks = raw_input.splitlines()
    groups = [backpacks[id: id+3] for id in range(0, len(backpacks), 3)]
    return sum(
        [priority(shared_item(group))for group in groups]
    )
