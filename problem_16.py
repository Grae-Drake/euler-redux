"""Solve Project Euler Problem 16.

Problem statement: 2^15 = 32768 and the sum of its digits is:
    3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16

"""


import argparse
from datetime import datetime


def solution(power: int) -> int:
    """Again, gotta love Python large number handling."""
    return sum([int(x) for x in str(2 ** power)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("power", help="power, default to 15", default=15,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.power)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.power))
    print("Execution time was {}.".format(clock_end - clock_start))
    