import unittest
import importlib
import json

def get_test_file(file):
    with open(f'data\\{file}', encoding="UTF-8") as f:
        raw_input = f.read()
    return raw_input

def get_test_data():
    with open("test_data.json", encoding="UTF-8") as f:
        test_data = json.load(f)
    return {tuple(map(int, key.split('-'))):answer for (key,answer) in test_data.items()}


class TestSolution(unittest.TestCase):

    def test_all_solutions(self):
        for ((day, part), answer) in get_test_data().items():
            raw_input = get_test_file(f'day_{day}_test.txt')
            with self.subTest(day=day, part=part):
                solution_module = importlib.import_module(f'solutions.day_{day}_part_{part}')
                self.assertEqual(solution_module.solution(raw_input), answer)


if __name__ == '__main__':
    unittest.main()
