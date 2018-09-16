"""Solve Project Euler Problem 15.

Problem statement: Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down, there are exactly 6 routes to the
bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?

https://projecteuler.net/problem=15

"""


import argparse
from datetime import datetime
from tools import choose


def solution(size: int) -> int:
    """Calculate number of paths for a given lattice size using combinatorics.
    
    The answer for grids of different sizes correspond to cells in Pascale's
    Triangle, and the value of cells in Paascale's traingle can be calculated
    directly (without needing recursion or memoization) with n choose k
    combinatorics.

    Specifically, the cell of Pascale's triangle we're interested in is the
    size * 2th row and the size'th column.
    
    """
    return choose(size * 2, size)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="size, default to 2", default=2,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.size)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.size))
    print("Execution time was {}.".format(clock_end - clock_start))
    