"""Solve Project Euler Problem 3.

Problem statement: The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

https://projecteuler.net/problem=3
"""

import argparse
from datetime import datetime
from tools import prime_sieve


def solution(limit: int) -> int:
    """Search candidate primes for the largest prime factor."""
    candidate_primes = prime_sieve(int(limit ** 0.5))
    for prime in reversed(candidate_primes):
        if (limit / prime) % 1 == 0:
            return prime
    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="number, default to 13195",
                    default=13195, type=int, nargs='?')
    args = parser.parse_args()
    start = datetime.now()
    answer = solution(args.number)
    end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.number))
    print("Execution time was {}.".format(end - start))
    