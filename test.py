import unittest
import importlib
from typing import Dict, Tuple, Any

def get_test_file(file):
    with open(f'data\\{file}') as F:
        raw_input = F.read()
    return raw_input

SOLUTIONS_TO_TEST = [(day, part) for day in range(1,26) for part in {1,2} if day in [7] and (day,part) != (25,2)]
ANSWERS: Dict[Tuple[int, int], Any] = {
    (7,1): 95437, 
    (7,2): 24933642, 
}

class TestSolution(unittest.TestCase):

    def test_all_solutions(self):
        for (day,part) in SOLUTIONS_TO_TEST:
            raw_input = get_test_file(f'day_{day}_test.txt')
            with self.subTest(day=day, part=part):
                solution_module = importlib.import_module(f'solutions.day_{day}_part_{part}')
                self.assertEqual(solution_module.solution(raw_input), ANSWERS[(day, part)])


if __name__ == '__main__':
    unittest.main()