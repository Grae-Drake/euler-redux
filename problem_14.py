"""Solve Project Euler Problem 14.

Problem statement: The following iterative sequence is defined for the set of
positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14

"""


import argparse
from datetime import datetime
from typing import Dict


def collatz(n: int, seen: Dict[int, int]) -> int:
    """Recursive function using to calculate the collatz number of n"""
    functs = {
        0: lambda x: int(x / 2),
        1: lambda x: x * 3 + 1
    }
    
    if seen.get(n):
        return seen[n]
    else:
        next_int = functs[n % 2](n)
        result = collatz(next_int, seen) + 1
        seen[n] = result
        return result


def solution(limit: int) -> int:
    """Docstring intro.

    Docstring body.
    
    """
    seen = {1: 1}
    for n in range(1, limit):
        collatz(n, seen)
    return max(seen.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 14", default=14,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    