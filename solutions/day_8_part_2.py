from itertools import repeat
from math import prod

def count_visible_trees(heights, tree_height, indices):
    number = 0
    for (x,y) in indices:
        number += 1
        if heights[x][y] >= tree_height:
            break
    return number

def scenic_score(heights, tree_y, tree_x):
    tree_height = heights[tree_y][tree_x]
    lines_of_sight = [
        zip(repeat(tree_y)               , reversed(range(0, tree_x))      ),
        zip(repeat(tree_y)               , range(tree_x+1, len(heights[0]))),
        zip(reversed(range(0, tree_y))   , repeat(tree_x)                  ),
        zip(range(tree_y+1, len(heights)), repeat(tree_x)                  ),
    ]
    return prod(
        count_visible_trees(heights, tree_height, indices) for indices in lines_of_sight
    )

def solution(raw_input: str):
    heights = [list(line) for line in raw_input.splitlines()]
    return max(scenic_score(heights, y, x) for y in range(0, len(heights)) for x in range(0, len(heights[0])))
