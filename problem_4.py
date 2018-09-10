"""Solve Project Euler Problem 4.

Problem statement: A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4
"""


import argparse
from datetime import datetime


def brute_force(start: int, limit: int) -> int:
    """Brute force solution. Solves in plenty of time."""
    result = 0
    search_space = range(start, limit)
    for x in search_space:
        for y in search_space:
            product = x * y
            if str(product) == str(product)[::-1]:
                result = max(result, product)
    return result


def backwards_search(start: int, limit: int) -> int:
    """Optimize brute force solution by starting with the large numbers."""
    result = 0
    floor = start
    search_space = range(start, limit)[::-1]
    for x in search_space:
        if x <= floor:
            break
        for y in search_space:
            product = x * y
            if str(product) == str(product)[::-1]:
                result = max(result, product)
                floor = max(floor, y)
                break
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 100", default=100,
                    type=int, nargs='?')
    parser.add_argument("start", help="start, default to 0", default=0,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = backwards_search(args.start, args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    