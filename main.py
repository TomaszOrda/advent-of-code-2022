import importlib
import sys


if __name__ == "__main__":
    DAY, PART = sys.argv[1], sys.argv[2]
    INPUT_FILE = f'data\\day_{DAY}.txt'

    with open(INPUT_FILE) as F:
        INPUT = F.read()
    
    solution_module = importlib.import_module(f'solutions.day_{DAY}_part_{PART}')

    print(solution_module.solution(INPUT))
