"""Solve Project Euler Problem 22.

Problem statement: Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

URL https://projecteuler.net/problem=22

"""


import argparse
from datetime import datetime
from string import ascii_uppercase


def name_score(name: str) -> int:
    """Sum the letter values of the input name."""
    alpha = dict([(char, i + 1) for (i, char) in enumerate(ascii_uppercase)])
    return sum([alpha[char] for char in name])


def solution(data_path: str) -> int:
    """Process the input data, sum the product of name scores and index."""
    with open(data_path) as f:
        names = sorted(f.readlines()[0].replace('"', '').split(','))

    return sum([i * name_score(name) for i, name in enumerate(names, 1)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", default='data/problem_22.txt', type=str,
                         nargs='?',
                         help="path to data, default to 'data/problem_22.txt'")
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.data_path)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.data_path))
    print("Execution time was {}.".format(clock_end - clock_start))
    