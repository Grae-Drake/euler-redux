"""Solve Project Euler Problem 5.

Problem statement: 2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

https://projecteuler.net/problem=5

"""


import argparse
from datetime import datetime
from tools import prime_factor_counts


def solution(limit: int) -> int:
    """Decompose range(1, 20) into prime factors, dedupe, and multiply."""
    all_prime_factors = []
    for x in range(1, limit + 1):
        factors = prime_factor_counts(x)
        all_prime_factors.append(factors or {x: 1})
    
    deduped_factors = {}
    for factor_set in all_prime_factors:
        for factor, count in factor_set.items():
            deduped_factors[factor] = max(deduped_factors.get(factor, 1), count)

    result = 1
    for factor, count in deduped_factors.items():
        result *= factor ** count
    return result


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
    