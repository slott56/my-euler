#!/usr/bin/env python3

# Prime generating integers
# =========================

# Problem 357

# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor, d, of 30, d+30/d is prime.
#
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

# ..  rubric:: Solution
# ..  py:module:: euler357
#     :synopsis: Prime generating integers

# Need :func:`divisors` function from :mod:`euler12`.

from euler12 import divisors

# Need prime test function based on simple set of primes to 10 000 000.
# Which is a lot of primes.

from euler46 import Primes

# Also need math.sqrt

import math

def all_divisors_prime(n, primes):
    """
    >>> all_primes= Primes()
    >>> divisors(30)
    [1, 2, 3, 5, 6, 10, 15, 30]
    >>> all_divisors_prime(30, all_primes)
    True
    """
    d_list= [d+n//d for d in divisors(n)]
    return all( primes.isPrime(x) for x in d_list[:len(d_list)//2+1] )

__test__ = {
    'test_answer': """
>>> all_primes = Primes()
>>> tgt = (n for n in range(2,31) if all_divisors_prime(n, all_primes))
>>> list(tgt)
[2, 6, 10, 22, 30]
>>> [d+2//d for d in divisors(2)]
[3, 3]
>>> [d+6//d for d in divisors(6)]
[7, 5, 5, 7]
>>> [d+10//d for d in divisors(10)]
[11, 7, 7, 11]
>>> [d+22//d for d in divisors(22)]
[23, 13, 13, 23]
>>> [d+30//d for d in divisors(30)]
[31, 17, 13, 11, 11, 13, 17, 31]
"""
}
# Solution.

def answer1():
    all_primes = Primes()
    tgt = (n for n in range(2,100000000) if all_divisors_prime(n, all_primes))
    print( list(tgt) )
    return sum(tgt)

def confirm( ans ):
    pass

# Create some output.

if __name__ == "__main__":
    import doctest, sys
    results= doctest.testmod()
    if results.failed: sys.exit(results.failed)

    ans= answer1()
    confirm( ans )
    print( "The sum of all ints such that for every divisor d of n, d+n/d is prime:", ans )