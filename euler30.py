#!/usr/bin/env python3

# Digit fifth powers
# ==================

# Problem 30

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# ..  math::
#
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    \\
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    \\
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As :math:`1 = 1^4` is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# ..  rubric:: Solution
# ..  py:module:: euler30
#     :synopsis: Digit fifth powers

# For each number in the range, i,
# Decompose the number into digits via a map( int, str(i) ),
# Compute the sum of the digits to the n power.

def powdigits( n ):
    """Generate all numbers for which sum of digits to the n power is the number.

    >>> from euler30 import powdigits
    >>> tuple( powdigits(4) )
    (1634, 8208, 9474)
    """
    # for n == 4, limit is 32805 5*9**4
    # for n == 5, limit is 354294 6*9**5
    for i in range(2,354294):
        digits_i= map( int, str(i) )
        s= sum( d**n for d in digits_i )
        if s == i:
            yield s

# Test the components in this module.

def test():
    import doctest
    doctest.testmod(verbose=0)
    assert ( 1634, 8208, 9474 ) == tuple( powdigits(4) )

# Compute the answer.

def answer():
    s= 0
    for i in powdigits(5):
        #print( i )
        s += i
    return s

# Confirm the answer.

def confirm(ans):
    assert 443839 == ans, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of all the numbers that can be written as the sum of fifth powers of their digits:", ans )