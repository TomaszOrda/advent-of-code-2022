import unittest
import importlib

def get_test_file(file):
    with open(f'data\\{file}', encoding="UTF-8") as f:
        raw_input = f.read()
    return raw_input

ANSWERS = {
    (1,1): 24000,
    (1,2): 45000,
    (7,1): 95437,
    (7,2): 24933642,
}

class TestSolution(unittest.TestCase):

    def test_all_solutions(self):
        for ((day, part), answer) in ANSWERS.items():
            raw_input = get_test_file(f'day_{day}_test.txt')
            with self.subTest(day=day, part=part):
                solution_module = importlib.import_module(f'solutions.day_{day}_part_{part}')
                self.assertEqual(solution_module.solution(raw_input), answer)



if __name__ == '__main__':
    unittest.main()
