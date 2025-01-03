import importlib
import sys


if __name__ == "__main__":
    DAY, PART = sys.argv[1].removeprefix("day").split("part")
    # TEST = "-test" in sys.argv or "--test" in sys.argv
    # INPUT_FILE = f'Day_{DAY}{ "_test" if TEST else "" }.txt'
    INPUT_FILE = f'data\\Day_{DAY}.txt'

    with open(INPUT_FILE) as F:
        INPUT = F.read()
    
    solution_module = importlib.import_module(f'solutions.day{DAY}part{PART}')

    print(solution_module.solution(INPUT))
