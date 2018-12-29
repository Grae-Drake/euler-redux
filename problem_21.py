"""Solve Project Euler Problem 21.

Problem statement: Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are:

    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    
The proper divisors of 284 are:

    1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21

"""


import argparse
from datetime import datetime
from tools import proper_divisors


def solution(limit: int) -> int:
    """Generate and sum all amicable pairs below limit."""
    proper_divisor_sums = {}
    amicable_pairs = []
    for x in range(1, limit):
        proper_divisor_sums[x] = sum(proper_divisors(x))
        next_step = proper_divisor_sums.get(proper_divisor_sums[x]) or 0
        if next_step == x and proper_divisor_sums[x] != x:
            amicable_pairs.append([x, proper_divisor_sums[x]])
    return sum([sum(x) for x in amicable_pairs])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 285", default=285,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    