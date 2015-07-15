#!/usr/bin/env python3

# Sub-string divisibility
# =======================

# Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
#
# Let :math:`d_1` be the 1\ :sup:`st` digit, :math:`d_2` be the 2\ :sup:`nd` digit, and so on. In this way, we note the following:
#
#    * :math:`d_2 d_3 d_4=406` is divisible by 2
#    * :math:`d_3 d_4 d_5=063` is divisible by 3
#    * :math:`d_4 d_5 d_6=635` is divisible by 5
#    * :math:`d_5 d_6 d_7=357` is divisible by 7
#    * :math:`d_6 d_7 d_8=572` is divisible by 11
#    * :math:`d_7 d_8 d_9=728` is divisible by 13
#    * :math:`d_8 d_9 d_{10}=289` is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# ..  rubric:: Solution
# ..  py:module:: euler43
#     :synopsis: Sub-string divisibility

# Some handy functions and classes we've already defined.
# :py:class:`euler24.Permutation`, :py:func:`euler04.digits`
# and :py:func:`euler35.number`.

from euler24 import Permutation
from euler04 import digits
from euler35 import number

# Define the substring divisibility property for a number.

def substringDivisibility( i ):
    """The substring divisibility property. The number
    is represented as a sequence of digits.

    >>> from euler43 import substringDivisibility
    >>> substringDivisibility( digits(1406357289) )
    True
    >>> substringDivisibility( digits(1406357298) )
    False
    """
    n2= number(i[1:4])
    n3= number(i[2:5])
    n5= number(i[3:6])
    n7= number(i[4:7])
    n11= number(i[5:8])
    n13= number(i[6:9])
    n17= number(i[7:10])
    test = (
        n2 % 2 == 0,
        n3 % 3 == 0,
        n5 % 5 == 0,
        n7 % 7 == 0,
        n11%11 == 0,
        n13%13 == 0,
        n17%17 == 0
    )
    return all( test )

# Generate all numbers with the substringDivisibility property.

def PDSD_gen():
    """Generate pan-digital numbers with the substring divisibility property.
    The number is represented as a sequence of digits.

    >>> from euler43 import PDSD_gen
    >>> numbers= list( PDSD_gen() )
    >>> 1406357289 in numbers
    True
    >>> numbers
    [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
    """
    pandigital10= Permutation(range(10))
    for i in pandigital10.nextPerm():
        if substringDivisibility(i):
            yield number(i)

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Compute the answer.

def answer():
    values= list( PDSD_gen() )
    return sum( values )

# Confirm the answer.

def confirm(ans):
    assert ans == 16695334890, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of all 0 to 9 pandigital numbers with this substring divisibility", ans )