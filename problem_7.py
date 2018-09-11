"""Solve Project Euler Problem XXXX.

Problem statement: By listing the first six prime numbers: 2, 3, 5, 7, 11,
and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7

"""


import argparse
import math
from datetime import datetime
from tools import prime_sieve


def nth_prime(n: int) -> int:
    """Find the nth prime number.

    This solution relies on the prime number theorem, which says that the
    nth prime number is close to n * ln(n). First we efficiently generate a
    list of primes less than n * ln(n) (plus a small buffer to account) for
    non-zero error, then efficiently look up the nth term in that list.
    
    """
    # This buffer offsets the shrinking error of pi(n) - n * ln(n).
    buffer = 3 if n < 6 else 1.5 if n < 100 else 1.2
    primes = prime_sieve(math.ceil(n * math.log(n) * buffer))
    return 2 if n == 1 else primes[n - 1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="nth prime number, default to 6", default=6,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = nth_prime(args.n)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.n))
    print("Execution time was {}.".format(clock_end - clock_start))
    