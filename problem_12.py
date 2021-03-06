"""Solve Project Euler Problem 12.

Problem statement: The sequence of triangle numbers is generated by adding the
natural numbers. So the 7th triangle number would be:

    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    
The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?

https://projecteuler.net/problem=12

"""


import argparse
from datetime import datetime
from typing import List
from tools import factors


def solution(limit: int) -> int:
    """Generate triangle numbers and their factors till we count 500."""
    triangle = 1
    n = 2
    while True:
        num_factors = len(factors(triangle))
        if num_factors > limit:
            return triangle
        triangle += n
        n += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 5", default=5,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    