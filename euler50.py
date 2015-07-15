#!/usr/bin/env python3

# Consecutive prime sum
# =====================

# Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
#
#     41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

# ..  rubric:: Solution
# ..  py:module:: euler50
#     :synopsis: Consecutive prime sum

# Two handy functions: :py:func:`euler10.makePrimes` and
# :py:func:`euler03.isprime`.

from euler10 import makePrimes
from euler03 import isprime

# A poor algorithm. Here for reference.
# This appears to be :math:`\textbf{O}(n^3)` on :samp:`len(primes)`.

def primesAsSumBad( upTo=1000000 ):
    primes= makePrimes(upTo)

    for t in primes:
        # Find a consecutive sequence of primes that sum to t.
        for start, sum in enumerate(primes):
            for p in range(start+1,len(primes)):
                sum += primes[p]
                if sum == t:
                    yield primes[start:p+1], t
                if sum > t: break

# A better algorithm.

def primesAsSum(upTo=1000000):
    primes= makePrimes(upTo)
    pSet= set( primes )
    topPrime= primes[-1]

    for start, sum in enumerate( primes ):
        i= start
        while sum <= topPrime and i+1 != len(primes):
            i += 1
            sum += primes[i]
            if sum in pSet:
                yield primes[start:i+1], sum

# Given primes as sums, what's the longest sequence of primes
# with a prime sum?

def longestPrimeAsSum( upTo=1000000 ):
    """
    >>> from euler50 import makePrimes, isprime, longestPrimeAsSum
    >>> primes= makePrimes(100)
    >>> all( isprime(p) for p in primes )
    True
    >>> longestPrimeAsSum( 100 )
    (6, [2, 3, 5, 7, 11, 13], 41)
    >>> longestPrimeAsSum( 1000 )
    (21, [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89], 953)
    """
    max_list = max( primesAsSum(upTo), key=lambda list_sum: len(list_sum[0]) )
    l, s = max_list
    return len(l), l, s

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Create the answer.

def answer():
    _, _, prime = longestPrimeAsSum(1000000)
    return prime

# Confirm the answer.

def confirm(ans):
    assert ans == 997651, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( ans )