#!/usr/bin/env python3

# Summation of primes
# ===================

# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# ..  rubric:: Solution
# ..  py:module:: euler10
#     :synopsis: Summation of primes

import math
import euler07

# ..  py:function:: makePrimes( lessThan )
#    Generate a list of primes less than 2,000,000
#    using :py:func:`euler07.primeGen`.
#
#    :param lessThan: Upper limit, inclusive.
#        Should be called lessThanOrEqualTo
#    :returns: list of primes

def makePrimes( lessThan ):
    """Make primes up to a limit.

    >>> from euler10 import makePrimes
    >>> sum(makePrimes(10))
    17
    """
    def primes(limit):
        for p in euler07.primeGen():
            if p >= limit: break
            yield p
    return list( primes(lessThan) )

# Test module components.

def test():
    import doctest
    doctest.testmod(verbose=0)
    doctest.testmod( euler07, verbose=0)

# Compute an answer for primes < 2,000,000

def answer():
   return sum(makePrimes(2000000))

# Confirm the answer.

def confirm(ans):
    assert ans == 142913828922, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of all the primes below two million:", ans )