#!/usr/bin/env python3

# ..  role:: hilight
#    :class: red-text
#
# ..  default-role:: hilight

# Path sum: two ways
# ==================

# Problem 81

# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
# by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# ..  parsed-literal::
#
#     `131`, 673, 234, 103,  18
#     `201`,  `96`, `342`, 965, 150
#     630, 803, `746`, `422`, 111
#     537, 699, 497, `121`, 956
#     805, 732, 524,  37, `331`
#
# Find the minimal path sum, in `matrix.txt <http://projecteuler.net/project/matrix.txt>`_ (right click and 'Save Link/Target As...'),
# a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
# by only moving right and down.

# ..  rubric:: Solution
# ..  py:module:: euler81
#     :synopsis: Path sum: two ways

import urllib.request
import csv
from io import StringIO
from pprint import pprint

# Parse a matrix to create a list-of-list struture.

def parse( text ):
    data = csv.reader( StringIO(text) )
    return [ list(map(int,row)) for row in data if len(row) != 0 ]

# Advance through the matrix, computing cell-by-cell totals of the
# minimum sum between above and left.

def advance( matrix ):
    sums = [ [0 for col in row] for row in matrix]
    sums[0][0]= matrix[0][0]
    for i in range(1,len(matrix)):
        # From 1 we want to visit (0,1), (1,1)  and (1,0), (1,1)
        # From 2 we want to visit (0,2), (1,2), (2,2) and (2,0), (2,1) and (2,2)
        for j in range(i+1):
            # Across the bottom: row i, column j
            above_left= []
            above_left.append( matrix[i][j] + sums[i-1][j] )
            if j != 0:
                above_left.append( matrix[i][j] + sums[i][j-1] )
            sums[i][j]= min( above_left )
        for j in range(i+1):
            # Down the side: row j, column i
            above_left= []
            if j != 0:
                above_left.append( matrix[j][i] + sums[j-1][i] )
            above_left.append( matrix[j][i] + sums[j][i-1] )
            sums[j][i]= min( above_left )
        #pprint( sums )
    return sums[-1][-1]

# Test the module components.

def test():
    """
    >>> test_matrix = '''
    ... 131, 673,     234,    103,     18
    ... 201, 96, 342, 965,     150
    ... 630,     803,    746, 422, 111
    ... 537,     699,    497,     121, 956
    ... 805,     732,    524,     37,      331
    ... '''
    >>> matrix= parse( test_matrix )
    >>> matrix
    [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
    >>> advance(matrix)
    2427
    """
    import doctest
    doctest.testmod(verbose=0)

def answer():
    #  "http://projecteuler.net/project/matrix.txt"
    matrix_txt= urllib.request.urlopen( "file:matrix.txt" ).read().decode("ASCII")
    matrix= parse( matrix_txt )
    return advance(matrix)

def confirm(ans):
    assert ans == 427337, "{0!r} Incorrect".format(ans)

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The minimal path sum of the given 80×80 matrix:", ans )
