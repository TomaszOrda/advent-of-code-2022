import importlib
import sys


if __name__ == "__main__":
    DAY, PART = sys.argv[1], sys.argv[2]
    # TEST = "-test" in sys.argv or "--test" in sys.argv
    # INPUT_FILE = f'Day_{DAY}{ "_test" if TEST else "" }.txt'
    INPUT_FILE = f'data\\day_{DAY}.txt'

    with open(INPUT_FILE) as F:
        INPUT = F.read()
    
    solution_module = importlib.import_module(f'solutions.day_{DAY}_part_{PART}')

    print(solution_module.solution(INPUT))
