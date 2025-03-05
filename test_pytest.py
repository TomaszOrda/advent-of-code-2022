import importlib
import json
import os
import pytest


def get_test_file(file):
    with open(f'data\\{file}', encoding="UTF-8") as f:
        raw_input = f.read()
    return raw_input


def get_test_data():
    with open("test_data.json", encoding="UTF-8") as f:
        test_data = json.load(f)
    return {tuple(map(int, key.split('-'))): answer for (key, answer) in test_data.items()}


@pytest.mark.parametrize("day,part", [(d, p) for d in range(1, 25) for p in [1, 2]] + [(25, 1)])
def test_solutions(day, part):
    # if day == 19:
    #     pytest.skip("Tests for day 19 skipped — long runtime")
    if not os.path.exists(f"solutions//day_{day}_part_{part}.py"):
        pytest.skip(f"Solution for day {day} part {part} does not exist")
    answer = get_test_data()[(day, part)]
    raw_input = get_test_file(f'day_{day}_test.txt')
    solution_module = importlib.import_module(f'solutions.day_{day}_part_{part}')
    result = solution_module.solution(raw_input)
    if result is None:
        pytest.skip(f"Solution for day {day} part {part} not implemented")
    assert result == answer
