"""Solve Project Euler Problem XXXX.

Problem statement: 

URL
"""

import argparse
from datetime import datetime
# from tools import something


def solution(limit: int) -> int:
    """Docstring intro.

    Docstring body.
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 10", default=10,
                    type=int, nargs='?')
    args = parser.parse_args()
    start = datetime.now()
    print(solution(args.limit))
    end = datetime.now()
    print("Execution time: {}".format(end - start))
    