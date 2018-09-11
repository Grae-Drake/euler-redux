"""Useful tools for Project Euler problems.

Exports:
    arithmetic_series_sum: Calculate the sum of an arithmetic series.
    prime_factor_counts: Decompose a number into all its prime factors.
    prime_sieve: Sieve of Erasthones to generate prime numbers.
    unique_prime_factors: List of unique prime factors.


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


def prime_factor_counts(n: int):
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


def prime_sieve(limit: int):
    """Generate primes below limit with the Sieve of Eratosthenes."""
    primes = [True] * limit
    i = 2
    while(i < limit):
        if primes[i]:
            for j in range(2 * i, limit, i):
                primes[j] = False
        i += 1
    
    return [i for i, val in list(enumerate(primes))[2:] if val]


def unique_prime_factors(n: int):
    """Return a sorted list of unique prime factors of n."""

    candidate_primes = prime_sieve(n)
    return [prime for prime in candidate_primes if n % prime == 0]