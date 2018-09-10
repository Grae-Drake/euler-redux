"""Solve Project Euler Problem 1.

Problem statement: If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
"""

import argparse
from datetime import datetime
from tools import arithmetic_series_sum


def brute_force(limit: int) -> int:
    """Solve the problem with a brute force loop.

    This problem is easily solved with a loop, and given the small limit
    there's no real need to optimize.
    """

    result = 0
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result


def constant_time(limit):
    """Solve the problem in constant time.

    Just because you don't _need_ to optimize doesn't mean you _can't_!
    This solution recognizes the three arithmetic series involved and
    calculates the result in constant time.
    """
    
    # Pardon the magic numbers, not going to generalize fizzbuzz :P
    last = limit - 1
    sum_threes = arithmetic_series_sum(3, (last // 3) * 3, last // 3)
    sum_fives = arithmetic_series_sum(5, (last // 5) * 5, last // 5)
    sum_fifteens = arithmetic_series_sum(15, (last // 15) * 15, last // 15)
    return sum_threes + sum_fives - sum_fifteens

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 10", default=10,
                    type=int, nargs='?')
    args = parser.parse_args()
    start = datetime.now()
    answer = constant_time(args.limit)
    end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(end - start))
