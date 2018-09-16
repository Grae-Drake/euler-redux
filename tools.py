"""Useful tools for Project Euler problems.

Exports:
    arithmetic_series_sum: Calculate the sum of an arithmetic series.
    nth_prime: Calculate the nth prime number.
    prime_factor_counts: Decompose a number into all its prime factors.
    prime_sieve: Sieve of Erasthones to generate prime numbers.
    unique_prime_factors: List of unique prime factors.


"""


import math
from typing import List, Dict


def arithmetic_series_sum(first_term: int, last_term: int, n: int) -> int:
    """Find the sum of an arithmetic series.
    
    Args:
        first_term: The first term in the arithmetic serires to be summed.
        last_term: The final term in the series.
        n: The number of terms in the series.

    Returns:
        The sum of the terms in the arithmetic series.

    """

    return int(n * (first_term + last_term) / 2)


def choose(n: int, k: int) -> int:
    """Efficiently calculate number of n choose k combinations."""
    result = 1
    for x in range(1, k + 1):
        result *= (n + 1 - x) / x
    return int(result)


def factors(n: int) -> List[int]:
    """Return a sorted list of unique factors of n, including 1 and n."""
    result = {1: True, n: True}
    for x in range(2, int(n ** .5)):
        if (n / x) % 1 == 0:
            result[x] = True
            result[int(n / x)] = True
    return sorted(result.keys())


def nth_prime(n: int) -> int:
    """Find the nth prime number.

    Args:
        n: the index of the prime number you'd like to find.
    
    Returns:
        the nth prime number.

    This solution relies on the prime number theorem, which says that the
    nth prime number is close to n * ln(n). First we efficiently generate a
    list of primes less than n * ln(n) (plus a small buffer to account) with
    a sieve of erasthones, then efficiently look up the nth term in that list.
    
    The buffer, which shrinks as the input increases, accounts for the
    shrinking error of the prime number theorem. This error could be modeled
    more closely for a small efficiency gain.
    
    """

    buffer = 3 if n < 6 else 1.5 if n < 100 else 1.2
    primes = prime_sieve(math.ceil(n * math.log(n) * buffer))
    return 2 if n == 1 else primes[n - 1]


def prime_factor_counts(n: int) -> Dict[int, int]:
    """Returns a dict with counts of all prime factors of n."""
    unique_factors = unique_prime_factors(n)
    result = {}
    for factor in unique_factors:
        factor_count = 1
        remainder = n / factor
        while ((remainder / factor) % 1 == 0):
            factor_count += 1
            remainder = remainder / factor
        result[factor] = factor_count
    return result


def prime_sieve(limit: int) -> List[int]:
    """Generate primes below limit with the Sieve of Eratosthenes."""
    primes = [True] * limit
    i = 2
    while(i < limit):
        if primes[i]:
            for j in range(2 * i, limit, i):
                primes[j] = False
        i += 1
    
    return [i for i, val in list(enumerate(primes))[2:] if val]


def product(lst: int) -> int:
    """Generate the product of all terms in a list."""
    result = 1
    for n in lst:
        result *= n
    return result


def unique_prime_factors(n: int) -> List[int]:
    """Return a sorted list of unique prime factors of n."""

    candidate_primes = prime_sieve(n)
    return [prime for prime in candidate_primes if n % prime == 0]
