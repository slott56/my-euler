#!/usr/bin/env python3

# Counting Sundays
# ==================

# Problem 19

# You are given the following information, but you may prefer to do some research for yourself.
#
# -   1 Jan 1900 was a Monday.
#
# -   Thirty days has September,
#
#     April, June and November.
#
#     All the rest have thirty-one,
#
#     Saving February alone,
#
#     Which has twenty-eight, rain or shine.
#
#     And on leap years, twenty-nine.
#
# -   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# ..  rubric:: Solution
# ..  py:module:: euler19
#     :synopsis: Counting Sundays

import datetime

# How many Sundays based on a simple enumeration of dates
# via the builtin :py:class:`datetime.date` class.

def sundays():
    for y in range(1901,2001):
        for m in range(1,13):
            d= datetime.date(y,m,1)
            if d.weekday() == 6:
                yield d

# Compute the answer.

def answer():
    return len(list(sundays()))

# Confirm the answer.

def confirm():
    assert answer() == 171

# Create some output.
if __name__ == "__main__":
    confirm()
    print( "The number of Sundays that fell on the first of the month during the twentieth century:", answer() )