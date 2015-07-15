#!/usr/bin/env python3

# Triangular, pentagonal, and hexagonal
# ======================================

# Problem 45

# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# - Triangle 	  	:math:`T_n=n(n+1)/2` 	  	1, 3,  6, 10, 15, ...
#
# - Pentagonal 	  	:math:`P_n=n(3n-1)/2` 	        1, 5, 12, 22, 35, ...
#
# - Hexagonal 	  	:math:`H_n=n(2n-1)` 	  	1, 6, 15, 28, 45, ...
#
# It can be verified that :math:`T_{285} = P_{165} = H_{143} = 40755`.
#
# Find the next triangle number that is also pentagonal and hexagonal.

# ..  rubric:: Solution
# ..  py:module:: euler45
#     :synopsis: Triangular, pentagonal, and hexagonal

# ..  py:function:: T(n)
#     Triangular number n
#
#     :param n: position in the sequence
#     :returns: :math:`T_n` triangular number n.

def T(n):
    return n*(n+1)//2

# ..  py:function:: P(n)
#     Pentagonal number n
#
#     :param n: position in the sequence
#     :returns: :math:`P_n` pentagonal number n.

def P(n):
    return n*(3*n-1)//2

# ..  py:function:: H(n)
#     Hexagonal number n
#
#     :param n: position in the sequence
#     :returns: :math:`H_n` hexagonal number n.

def H(n):
    return n*(2*n-1)

# Test the module components.

def test():
    """
    >>> from euler45 import T, P, H
    >>> P(165)
    40755
    >>> T(285)
    40755
    >>> H(143)
    40755
    """
    import doctest
    doctest.testmod(verbose=0)
    assert T(285) == P(165)
    assert T(285) == H(143)
    assert P(165) == H(143)

# Create the answer.

def answer():
    t, p, h = 286, 165, 143
    while P(p) != T(t) or H(h) != T(t):
        if P(p) < T(t):
            p += 1
        elif H(h) < T(t):
            h += 1
        else:
            t += 1
    assert P(p) == T(t) and H(h) == T(t)
    # print( t, T(t), "==", p, P(p), "==", h, H(h) )
    return T(t)

# Confirm the answer.

def confirm( ans ):
    assert ans == 1533776805, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm( ans )
    print( "The triangle number that is also pentagonal and hexagonal:", ans )