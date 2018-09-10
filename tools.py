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