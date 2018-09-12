"""Solve Project Euler Problem XXXX.

Problem statement: The four adjacent digits in the 1000-digit number in
data/problem8.txt that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?

https://projecteuler.net/problem=8

"""


import argparse
from datetime import datetime
from tools import product

    
def get_data(data):
    """Load and process the input data."""
    with open(data) as f:
        read_data = f.read().replace('\n', '')
    return [int(char) for char in read_data]
    

def brute_force(window: int, data: str):
    """Brute force O(m * n) solution runs in plenty of time."""
    digits = get_data(data)
    max_product = product(digits[0:window])
    for x in range(1, len(digits) - window + 1):
        max_product = max(max_product, product(digits[x:x + window]))
    return max_product


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("window", help="window, default to 4", default=4,
                    type=int, nargs='?')
    parser.add_argument("data", help="data, default to data/problem_8.txt",
                    default="data/problem_8.txt", type=str, nargs='?')
    args = parser.parse_args()  
    clock_start = datetime.now()
    answer = brute_force(args.window, args.data)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.window))
    print("Execution time was {}.".format(clock_end - clock_start))
    