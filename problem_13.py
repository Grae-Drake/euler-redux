"""Solve Project Euler Problem 13.

Problem statement: Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers [located in data/problem_13.txt].

https://projecteuler.net/problem=13

"""


import argparse
from datetime import datetime


def solution(window: int, data_path: str) -> str:
    """Simple addition. No need to worry about number size with Python :D"""
    with open(data_path) as f:
        numbers = [int(line) for line in f.readlines()]
    return str(sum(numbers))[:10]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("window", help="window, default to 10", default=10,
                    type=int, nargs='?')
    parser.add_argument("data_path", type=str, nargs='?',
                        default='data/problem_13.txt', 
                        help="data path, default to data/problem 13.txt")
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.window, args.data_path)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.window))
    print("Execution time was {}.".format(clock_end - clock_start))
    