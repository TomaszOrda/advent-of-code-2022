from itertools import repeat


def visible(heights, tree_y, tree_x):
    height = heights[tree_y][tree_x]
    lines_of_sight = [
        zip(repeat(tree_y), range(0, tree_x)),
        zip(repeat(tree_y), range(tree_x+1, len(heights[0]))),
        zip(range(0, tree_y), repeat(tree_x)),
        zip(range(tree_y+1, len(heights)), repeat(tree_x)),
    ]
    return any(
        all(heights[y][x] < height for y, x in indices) for indices in lines_of_sight
    )


def solution(raw_input: str):
    heights = [list(line) for line in raw_input.splitlines()]
    return sum(visible(heights, y, x) for y in range(0, len(heights)) for x in range(0, len(heights[0])))
