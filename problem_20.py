"""Solve Project Euler Problem 20.

Problem statement: n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20

"""


import argparse
import math
from datetime import datetime


def solution(limit: int) -> int:
    """Again, Python just _handles_ large numbers FTW.

    An alternative might be to keep track of the running product and to modulo
    out factors of 10 to remove zeros to the right. But there's no need here:
    this solution gives the right answer in ~4 seconds for 100,000 factorial.
    
    """
    return sum([int(digit) for digit in str(math.factorial(limit))])


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
    