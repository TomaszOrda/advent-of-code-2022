import importlib
import sys


if __name__ == "__main__":
    day, part = sys.argv[1], sys.argv[2]
    input_file = f'data\\day_{day}.txt'

    with open(input_file, encoding="UTF-8") as f:
        raw_input = f.read()

    solution_module = importlib.import_module(f'solutions.day_{day}_part_{part}')

    print(solution_module.solution(raw_input))
