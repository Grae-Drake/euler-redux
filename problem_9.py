"""Solve Project Euler Problem 9.

Problem statement: A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9

"""


import argparse
from datetime import datetime
# from tools import something


def solution(limit: int) -> int:
    """Generate triples using Euclid's formula till we find the solution."""
    for m in range(2, limit):
        for n in range(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == limit:
                return a * b * c


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 12", default=12,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    