"""Solve Project Euler Problem 19.

Problem statement: You are given the following information, but you may prefer
to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

https://projecteuler.net/problem=19

"""


import argparse
from datetime import datetime


def solution() -> int:
    """Calculate the number of Sundays on the first of the month."""
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = []
    for year in range(1900, 2001):
        for month in range(12):
            if month == 1 and year % 4 == 0 and year % 400 != 0:
                days = 29
            else:
                days = months[month]
            for day in range(1, days + 1):
                dates.append({'day': day, 'month': month + 1, 'year': year})
    
    result = 0
    for date in dates[371::7]:
        if date['day'] == 1:
            result += 1
    return result


if __name__ == "__main__":
    clock_start = datetime.now()
    answer = solution()
    clock_end = datetime.now()
    print("{} Sundays fell on the first of the month during the 20th century.".format(answer))
    print("Execution time was {}.".format(clock_end - clock_start))
    