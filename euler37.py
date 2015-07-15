#!/usr/bin/env python3

# Truncatable primes
# ==================

# Problem 37

# The number 3797 has an interesting property. Being prime itself, it is possible
# to continuously remove digits from left to right, and remain prime at each
# stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
# 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# ..  rubric:: Solution
# ..  py:module:: euler37
#     :synopsis: Double-base palindromes

# Use :py:func:`euler03.isprime`

from euler03 import isprime
import math

# Arithmetic truncation.
# We could have have used
# the str(n) to pick apart various substrings.

def leftTrunc( n ):
    """Yields all left-truncation values.

    >>> from euler37 import leftTrunc
    >>> list( leftTrunc( 3797 ) )
    [3797, 797, 97, 7]
    """
    mask= 10**(1+int(math.log10( n )))
    while mask != 1:
        yield n%mask
        mask = mask // 10

def rightTrunc( n ):
    """Yields all right-truncation values.

    >>> from euler37 import rightTrunc
    >>> list( rightTrunc( 3797 ) )
    [3797, 379, 37, 3]
    """
    while n != 0:
        yield n
        n =  n // 10

# Filter for left and right truncated prime.

def lrTruncPrime( n ):
    """Is n both left-trunc and right trunc prime?

    >>> from euler37 import lrTruncPrime
    >>> lrTruncPrime(3797)
    True
    >>> lrTruncPrime(997)
    False
    """
    lt= all( isprime(t) for t in leftTrunc(n) )
    rt= all( isprime(t) for t in rightTrunc(n) )
    return lt and rt

# Generate primes which fit the requirements.

def LRTP_gen(count=11):
    """
    >>> from euler37 import LRTP_gen
    >>> list( LRTP_gen() )
    [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    """
    n= 11
    while count != 0:
        if lrTruncPrime(n):
            count -= 1
            yield n
        n += 2

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)
    assert [3797, 797, 97, 7] == list ( leftTrunc( 3797 ) )
    assert [3797, 379, 37, 3] == list( rightTrunc( 3797 ) )

# Create the answer.

def answer():
    l= list( LRTP_gen() )
    #print( l )
    return( sum( l ) )

# Confirm the answer.

def confirm(ans):
    assert ans == 748317, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of the only eleven primes that are both truncatable from left to"
        " right and right to left:", ans )