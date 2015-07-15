#!/usr/bin/env python3

# Double-base palindromes
# =======================

# Problem 36

# The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# ..  rubric:: Solution
# ..  py:module:: euler36
#     :synopsis: Double-base palindromes

# Use :py:func:`euler04.palindrome`.

from euler04 import palindrome

def pal_2_10():
    for n in range(1000000):
        if palindrome( n, 2 ) and palindrome( n, 10 ):
            yield n

# Test the module components.

def test():
    """
    >>> from euler04 import palindrome
    >>> palindrome( 585 )
    True
    >>> palindrome( int('1001001001',2) )
    True
    >>> palindrome( 585, 2 )
    True
    >>> palindrome( 585, 10 )
    True
    >>> palindrome( 5, 10 )
    True
    >>> palindrome( 5, 2 )
    True
    """
    import doctest
    doctest.testmod(verbose=0)

# Create the answer.

def answer():
    pals = list( pal_2_10() )
    #print( pals )
    return sum(pals)

# Confirm the answer.

def confirm(ans):
    assert 872187 == ans, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The sum of all numbers, less than one million, which are palindromic in base 10 and base 2:", ans )