#!/usr/bin/env python3

# ..  role:: hilight
#    :class: red-text
#
# ..  default-role:: hilight

# ..  _problem18:

# Maximum path sum I
# ===================

# Problem 18

# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#
# ..  parsed-literal::
#
#         `3`
#        `7` 5
#       2 `4` 6
#      8 5 `9` 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# ..  parsed-literal::
#
#                   75
#                  95 64
#                 17 47 82
#                18 35 87 10
#               20 04 82 47 65
#              19 01 23 75 03 34
#             88 02 77 73 07 63 67
#            99 65 04 28 06 16 70 92
#           41 41 26 56 83 40 80 70 33
#          41 48 72 33 47 32 37 16 94 29
#         53 71 44 65 25 43 91 52 97 51 14
#        70 11 33 28 77 73 17 78 39 68 17 57
#       91 71 52 38 17 14 91 43 58 50 27 29 48
#      63 66 04 68 89 53 67 30 73 16 69 87 40 31
#     04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this
# problem by trying every route. However, :ref:`problem67`, is the same
# challenge with a triangle containing one-hundred rows; it cannot
# be solved by brute force, and requires a clever method! ;o)

# ..  rubric:: Solution
# ..  py:module:: euler18
#     :synopsis: Maximum path sum I

# The triangle to process.

t15_text= """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
t15= [ list(map(int, x.split())) for x in t15_text.strip().splitlines() ]
assert 15 == len(t15)

# Path Up a Triangle

def pathUp( triangle ):
    """
    >>> t4= [
    ... (3,),
    ... (7, 5),
    ... (2, 4, 6),
    ... (8, 5, 9, 3),
    ... ]
    ...
    >>> pathUp(t4)
    23
    """
    triangle= list(reversed(triangle))
    pathLen= triangle[0] # Each bottom row item is an initial value for the length.
    for row in range(1,len(triangle) ):
        newPath= []
        for col in range(len(triangle[row])):
            sl= triangle[row][col]+pathLen[col]
            sr= triangle[row][col]+pathLen[col+1]
            newPath.append( max(sl,sr) )
        pathLen= newPath
    return pathLen[0]

# Test the components.

def test():
    import doctest
    doctest.testmod(verbose=0)

# Compute the answer.

def answer():
    return pathUp( t15 )

# Confirm the answer.

def confirm(ans):
    assert ans == 1074, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The maximum total from top to bottom of the given triangle:", ans)