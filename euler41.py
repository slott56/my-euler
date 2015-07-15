#!/usr/bin/env python3

# Pandigital prime
# ================

# Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
#
# What is the largest n-digit pandigital prime that exists?

# ..  rubric:: Solution
# ..  py:module:: euler41
#     :synopsis: Pandigital prime

# Some handy functions and classes we've already defined.
# :py:class:`euler24.Permutation`, :py:func:`euler03.isprime`
# and :py:func:`euler35.number`.

from euler24 import Permutation
from euler03 import isprime
from euler35 import number

# Create all permutations of a given set of digits.

def pandigitalPrimes(size):
    """Generate all pan-digital primes of a given size.

    >>> from euler41 import pandigitalPrimes
    >>> pd4 = list( pandigitalPrimes(4) )
    >>> 2143 in pd4
    True
    >>> pd4
    [1423, 2143, 2341, 4231]
    """
    permN= Permutation( range(1,size+1) )
    for p in permN.nextPerm():
        ld= p[-1]
        if ld % 2 == 0: continue # skip even numbers
        if ld == 5: continue # skip 5's, also
        n= number( p )
        if isprime(n):
            yield n

# For sizes from 1 digit to 9 digits, generate all pan-digital primes.
# The max should surface quickly if we go in descending order.

def PDP_gen():
    for n in range(9,0,-1):
        for pd in pandigitalPrimes(n):
            yield pd

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Compute the answer.

def answer():
    return max( PDP_gen() )

# Confirm the answer.

def confirm(ans):
    assert ans == 7652413, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The largest pan-digital prime:", ans )
