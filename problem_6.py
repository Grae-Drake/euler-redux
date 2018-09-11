"""Solve Project Euler Problem 6.

Problem statement: The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

https://projecteuler.net/problem=6
"""


import argparse
from datetime import datetime
# from tools import something


def solution(limit: int) -> int:
    """Square of sum minus sum of squares."""
    ints = range(1, limit + 1)
    return sum(ints) ** 2 - sum([x ** 2 for x in ints])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 10", default=10,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    