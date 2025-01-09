def touching(head, tail):
    return max(abs(head[0]-tail[0]), abs(head[1]-tail[1])) <= 1


ROPE_LENGTH = 10
HEAD_SEGMENT = ROPE_LENGTH-1
TAIL_SEGMENT = 0

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


def tug(rope, segment):
    if segment < 0:
        return None
    if touching(rope[segment], rope[segment+1]):
        return None

    dist_x = rope[segment+1][0]-rope[segment][0]
    dist_y = rope[segment+1][1]-rope[segment][1]

    if abs(dist_x) == 2 and dist_y == 0:
        rope[segment] = rope[segment][0] + dist_x//2, rope[segment][1]
    elif abs(dist_y) == 2 and dist_x == 0:
        rope[segment] = rope[segment][0], rope[segment][1] + dist_y//2
    else:
        # Diagonal case
        rope[segment] = rope[segment][0] + dist_x//abs(dist_x), rope[segment][1] + dist_y//abs(dist_y)

    tug(rope, segment-1)


def solution(raw_input: str):
    moves = [move.split() for move in raw_input.splitlines()]
    rope = {segment: (0, 0) for segment in range(ROPE_LENGTH)}

    visited = set()
    visited.add((0, 0))
    for (direction, times) in moves:
        for _ in range(int(times)):
            rope[HEAD_SEGMENT] = move(rope[HEAD_SEGMENT], DIR[direction])
            tug(rope, HEAD_SEGMENT-1)
            visited.add(rope[TAIL_SEGMENT])

    return len(visited)
