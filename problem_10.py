"""Solve Project Euler Problem 10.

Problem statement: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

"""


import argparse
from datetime import datetime
from tools import prime_sieve


def solution(limit: int) -> int:
    """Use sieve of Erasthones to efficiently generate primes."""
    return sum(prime_sieve(limit))


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
    