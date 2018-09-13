"""Solve Project Euler Problem 11.

Problem statement: In the 20×20 grid below, four numbers along a diagonal
line have been marked in red. [See data/problem_11.txt]

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?

https://projecteuler.net/problem=11

"""


import argparse
from datetime import datetime


def default(matrix, x: int, y: int, default: int):
    """Helper function to handle out of index lookups on the data"""
    try:
        return matrix[x][y]
    except IndexError:
        return default


def get_data(data_path: str):
    with open(data_path) as f:
        read_data = [[int(n) for n in l.strip().split(' ')] for l in list(f)]
    return read_data


def solution(window: int, data_path: str) -> int:
    """For each term, look at the 4 sets of adjacent numbers."""
    data = get_data(data_path)
    max_product = 0
    for row in range(len(data)):
        for column in range(len(data[0])):
            h_product = 1
            v_product = 1
            d_up_product = 1
            d_down_product = 1
            for x in range(window):
                # Consider any out of index terms to be 0.
                h_product *= default(data, row, column + x, 0)
                v_product *= default(data, row + x, column, 0)
                d_up_product *= default(data, row - x, column + x, 0)
                d_down_product *= default(data, row + x, column + x, 0)
            max_product = max(max_product, h_product, v_product, d_up_product,
                              d_down_product)
    return max_product


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("window", help="window, default to 4", default=4,
                        type=int, nargs='?')
    parser.add_argument("data_path", default="data/problem_11.txt", type=str,
                        help="path to data, default to data/problem_11.txt",
                        nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.window, args.data_path)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.window))
    print("Execution time was {}.".format(clock_end - clock_start))
    