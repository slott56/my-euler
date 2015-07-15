#!/usr/bin/env python3

# Highly divisible triangular number
# ==================================

# Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. So
# the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
# terms would be:
#
#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
# ..  parsed-literal::
#
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

# ..  rubric:: Solution
# ..  py:module:: euler12
#     :synopsis: Highly divisible triangular number

import math
import collections

# Compute prime factors of a number.

class Factorize:
    """Prime factors with memoization of answers.
    Returns a dictionary of factors and their frequency.

    >>> from euler12 import Factorize
    >>> f = Factorize()
    >>> sorted(f(28).items())
    [(2, 2), (7, 1)]
    """
    def __init__( self ):
        self.memo= {}
    def __call__( self, x ):
        if x not in self.memo:
            new= collections.defaultdict(int)
            self.factor( x, new )
            self.memo[x]= new
        return self.memo[x]
    def factor( self, x, facts ):
        if x in self.memo:
            facts.update(self.memo[x])
            return
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                facts[i] += 1
                self.factor( x//i, facts )
                return
        facts[x] += 1

# ..  py:function:: factors( x )
#     Returns the prime factors of x
#
#     :param x: number to factor
#     :returns: dictionary with factor and count of occurrences.

factors= Factorize()

# ..  py:function:: divisors( x )
#     Returns all divisors of x
#
#     :param x: number to factor
#     :returns: list of divisors
#
# Compute divisors of a number, including 1 and the number.

def divisors( x ):
    """
    >>> from euler12 import divisors
    >>> divisors(28)
    [1, 2, 4, 7, 14, 28]
    """
    return [1] + [ i for i in range(2,x//2+1) if x%i == 0 ] + [x]

# ..  py:function:: len_divisors( factors )
#     Compute the number of divisors based on the factors
#     and their frequecies.
#
#     A number like 8, for example would have factors of {2: 3},
#     which has a len of 3. There are 4 divisors: 1, 2, 4, and 8.
#     We don't actually compute all the divisors, that takes too long.
#
#     :param factors: output from :py:func:`factors`:
#         a dictionary of factor and frequency
#     :returns: the number of divisors

def len_divisors( factors ):
    """
    >>> from euler12 import len_divisors, factors
    >>> len_divisors( factors( 28 ) )
    6
    """
    prod= 1
    for v in factors.values():
        prod *= (v+1)
    return prod

# Generate ascending sequence of triangle numbers, and the number
# of divisors using :py:func:`factors` and :py:func:`len_divisors`.
# This could have been done with :py:func:`divisors`, but that's
# too slow.

def triangle_gen():
    """
    >>> from euler12 import triangle_gen
    >>> tg= triangle_gen()
    >>> [ next(tg) for i in range(7) ]
    [(1, 1, 2), (2, 3, 2), (3, 6, 4), (4, 10, 4), (5, 15, 4), (6, 21, 4), (7, 28, 6)]
    """
    o = 1
    triangle= 0
    while True:
        triangle += o
        f= factors(triangle)
        d= len_divisors(f)
        yield o, triangle, d
        o += 1

# Simple process for getting the triangle number with the most
# divisors.

def simple(limit=500):
    """
    >>> from euler12 import simple
    >>> simple(5)
    28
    """
    tg= triangle_gen()
    while True:
        o, triangle, d = next(tg)
        if d > limit:
            return triangle

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Compute the answer.

def answer():
    return simple(500)

# Confirm the answer.

def confirm(ans):
    assert ans == 76576500, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The value of the first triangle number to have over five hundred divisors:", ans )