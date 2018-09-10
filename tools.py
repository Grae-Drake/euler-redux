"""Useful tools for Project Euler problems.

Exports:
    arithmetic_series_sum: calculate the sum of an arithmetic series.
"""

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


def prime_factors(n: int):
    """Return a sorted list of unique prime factors of n."""

    candidate_primes = prime_sieve(int(n ** 0.5))
    return [prime for prime in candidate_primes if n % prime == 0]


def prime_sieve(limit: int):
    # """Generate primes below limit with the Sieve of Eratosthenes."""
    primes = [True] * limit
    i = 2
    while(i < limit):
        if primes[i]:
            for j in range(2 * i, limit, i):
                primes[j] = False
        i += 1
    return [i for i, val in list(enumerate(primes))[2:] if val]