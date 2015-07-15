#!/usr/bin/env python3

# Integer right triangles
# =======================

# Problem 39

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
#     {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# Define an exception we can raise to exit a loop.

# ..  py:exception:: DomainError
#     The number has no integer square root.

class DomainError( Exception ):
    pass

# An integer square root operation that maps
# numbers from 0 to 1000 to their square root,
# if it's an integer. Otherwise, a :py:exc:`DomainError` is raised.

ROOTS = dict( (d*d,d) for d in range(1000) )
def intSqrt( n ):
    """Integer square root or :py:exc:`DomainError` if there
    is no integer square root.

    >>> from euler39 import intSqrt, DomainError
    >>> intSqrt(9)
    3
    >>> intSqrt(10)
    Traceback (most recent call last):
    ...
    euler39.DomainError: No integer square root of 10
    """
    try:
        return ROOTS[n]
    except KeyError:
        raise DomainError( "No integer square root of {0}".format(n) )

# Generate right triangles with integral length sides that have the
# required perimeter. It's handy to have the details to confirm
# the algorithm. We don't really need the tuple, however,
# since all we really want is a count.

def rightTriangles( p ):
    """Generate all possible triangles for a given perimeter.

    >>> from euler39 import rightTriangles
    >>> list(rightTriangles(120))
    [(20, 48, 52), (24, 45, 51), (30, 40, 50)]
    """
    for a in range(1,p+1):
        for b in range(a,p):
            try:
                c= intSqrt(a*a+b*b)
                if a+b+c == p:
                    yield a,b,c
            except DomainError:
                pass

# Generate all triangle lists for all perimeter values from 0 to 1000.
# Note that we don't really use the triangles themselves; we only
# really wanted the count.

# We might want to define our own `count()` function instead of `len()`.
# :code:`sum( 1 for t in rightTriangles(p) )` for example, which
# doesn't create a list object.

def triangles_for_P_gen( limit=1000 ):
    for p in range(limit):
        rt= list(rightTriangles(p))
        yield len(rt), p

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)
    rt120= list(rightTriangles(120))
    #print( rt120 )
    assert len(rt120) == 3

# Compute the answer.

def answer():
    len_, p = max( triangles_for_P_gen() )
    return p

# Confirm the answer.

def confirm(ans):
    assert ans == 840, "{0!r} Incorrect".format(ans)

# Create the output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The perimeter with the maximum number of integral length sides:", ans )