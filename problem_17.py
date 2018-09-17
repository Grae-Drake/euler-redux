"""Solve Project Euler Problem 17.

Problem statement: If the numbers 1 to 5 are written out in words: one, two,
three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

URL

"""


import argparse
from datetime import datetime


def solution(limit: int) -> int:
    """Generate English representations and sum lengths."""

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
            'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']
    
    
    def britify(n: int) -> str:
        """Convert n to British English representation, omit spaces etc."""
        if n == 1000:
            return 'onethousand'
        else:
            result = ''
            hundred_count = n // 100
            if hundred_count:
                result += ones[hundred_count] + 'hundred'
            mod_100 = n % 100
            if hundred_count and n % 100:
                result += 'and'
            if mod_100 < 20:
                result += ones[mod_100]
            else:
                result += tens[mod_100 // 10]
                result += ones[n % 10]
            return result
    
    
    return sum([len(britify(x)) for x in range(1, limit + 1)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", help="limit, default to 5", default=5,
                    type=int, nargs='?')
    args = parser.parse_args()
    clock_start = datetime.now()
    answer = solution(args.limit)
    clock_end = datetime.now()
    print("The answer is {} for input {}.".format(answer, args.limit))
    print("Execution time was {}.".format(clock_end - clock_start))
    