from collections import deque
import numpy as np

MAX_INT32 = np.iinfo(np.int32).max


def neighbors(height_map, position):
    result = []
    for vec in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_position = (position[0] + vec[0], position[1] + vec[1])
        if new_position[0] >= 0 and new_position[0] < len(height_map) and \
                new_position[1] >= 0 and new_position[1] < len(height_map[0]):
            result.append(new_position)
    return result


def height(height_map, pos):
    if height_map[pos] == 'S':
        return ord('a')
    if height_map[pos] == 'E':
        return ord('z')
    return ord(height_map[pos])


def reachable(height_map, from_pos, to_pos):
    return height(height_map, from_pos) >= height(height_map, to_pos) - 1


def solution(raw_input: str):

    height_map = np.asarray([list(line) for line in raw_input.splitlines()])
    start_position = next(zip(*np.where('S' == height_map)))
    end_position = next(zip(*np.where('E' == height_map)))

    distance_map = np.full_like(height_map, MAX_INT32, dtype=np.int32)
    distance_map[start_position] = 0

    # We need efficient appendleft for BFS here
    queue = deque([start_position])

    while queue:
        position = queue.pop()
        for neighbor in neighbors(height_map, position):
            if reachable(height_map, position, neighbor):
                if distance_map[neighbor] > distance_map[position] + 1:
                    distance_map[neighbor] = distance_map[position] + 1
                    queue.appendleft(neighbor)

    return distance_map[end_position]
