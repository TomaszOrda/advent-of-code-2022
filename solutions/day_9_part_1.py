def distance(head, tail):
    return max(abs(head[0]-tail[0]), abs(head[1]-tail[1]))


DIR = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def move(head, direction):
    x = head[0] + direction[0]
    y = head[1] + direction[1]
    return (x, y)


def solution(raw_input: str):
    moves = [move.split() for move in raw_input.splitlines()]

    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add((0, 0))
    for (direction, times) in moves:
        for _ in range(int(times)):
            head_ghost = head
            head = move(head, DIR[direction])
            if distance(head, tail) > 1:
                tail = head_ghost
                visited.add(tail)

    return len(visited)
