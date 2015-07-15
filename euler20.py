#!/usr/bin/env python3

# Factorial digit sum
# ===================

# Problem 20

# n! means n × (n - 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# ..  rubric:: Solution
# ..  py:module:: euler20
#     :synopsis: Factorial digit sum

# See :py:func:`euler16.pow2_digits` for another implementation of this digit-based
# multiplication.

# ..  py:class:: Product
#     Multiply numbers, creating a sequence of digits.
#
#     This implements the in-place p \*= n operator.

class Product:
    def __init__( self ):
        self.digits= [ 1 ]
    def mult( self, n ):
        carry= 0
        for i,d in enumerate(self.digits):
            d2= n*d+carry
            self.digits[i]= d2 % 10
            carry = d2 // 10
        while carry != 0:
            self.digits.append(carry%10)
            carry= carry//10
    def value( self ):
        return list( reversed( self.digits ) )

# Use :py:class:`Product` to accumulate the digits for n!

def factDigits(n):
    """
    >>> from euler20 import factDigits
    >>> factDigits(10)
    [3, 6, 2, 8, 8, 0, 0]
    >>> sum(factDigits(10))
    27
    """
    p= Product()
    for i in range(1,n+1):
        p.mult(i)
    return p.value()

# Test the module's components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Compute the answer.

def answer():
    f100= factDigits(100)
    return sum(f100)

# Confirm the answer.

def confirm(ans):
    assert ans == 648, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of the digits in the number 100!:", ans )