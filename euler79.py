#!/usr/bin/env python3

# Passcode derivation
# ====================

# Problem 79

# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278, they
# may asked for the 2nd, 3rd, and 5th characters; the expected reply would be:
# 317.
#
# The text file, `keylog.txt <http://projecteuler.net/project/keylog.txt>`_, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file
# so as to determine the shortest possible secret passcode of unknown length.

# ..  rubric:: Solution
# ..  py:module:: euler79
#     :synopsis: Passcode derivation

# Essentially, this is a topological sort/merge.

# Each successful attempt gives us a partial ordering of digits.  When we
# merge all the partial orders, we get a total order.  We can then remove
# duplicates.
#
# Each new number can be merged into the total order or has to be deferred because
# we can't match any digits with our total order.

from collections import defaultdict
import urllib.request

# A class to define the ordering of a before b.

class Before:
    def __init__( self, a, b ):
        self.a= a
        self.b= b
    def __repr__( self ):
        return "%s < %s" % ( self.a, self.b )
    def __hash__( self ):
        return hash( ( self.a, self.b ) )
    def __eq__( self, other ):
        return self.a == other.a and self.b == other.b

# Create :py:class:`Before` pairs from a list of the 3-character subsequences.
# Each a, b, c sequence is an a,b and b,c ordering.

def makePairs( aList ):
    """
    >>> sample= [ [2,4,6], [1,3,5], [1, 2, 3], [2, 3, 5], [3, 5, 4] ]
    >>> rules= makePairs( sample )
    >>> [ (k,rules[k]) for k in sorted(rules) ]
    [(1, [1 < 3, 1 < 2]), (2, [2 < 4, 2 < 3]), (3, [3 < 5]), (4, [4 < 6]), (5, [5 < 4])]
    """
    ruleDict= defaultdict(list)
    for subseq in aList:
        for i in range(len(subseq)-1):
            rule= Before( subseq[i], subseq[i+1] )
            if rule not in ruleDict[rule.a]:
                ruleDict[rule.a].append( rule )
    return ruleDict

# Topological sort among all :py:class:`Before` orderings.

def topoSort( ruleDict ):
    """
    >>> sample= [ [2,4,6], [1,3,5], [1, 2, 3], [2, 3, 5], [3, 5, 4] ]
    >>> ruleDict= makePairs( sample )
    >>> list( topoSort(ruleDict) )
    [1, 2, 3, 5, 4, 6]
    """
    last= None
    while len(ruleDict) != 0:
        bValues= [ r.b for rList in ruleDict.values() for r in rList ]
        aValues= [ r.a for rList in ruleDict.values() for r in rList ]
        topSet = set( aValues ) - set( bValues )
        last= set( bValues ) - set( aValues )
        if len(topSet) != 1:
            raise Exception( "Unsortable" )
        top= topSet.pop()
        yield top
        del ruleDict[top]
    yield last.pop()

# Test the module components.

def test():
    import doctest
    doctest.testmod(verbose=0)

    sample= [ [2,4,6], [1,3,5], [1, 2, 3], [2, 3, 5], [3, 5, 4] ]
    ruleDict= makePairs( sample )
    #print ruleDict
    assert [1,2,3,5,4,6] == list( topoSort(ruleDict) )

# Compute the answer.

def answer():
    # 'http://projecteuler.net/project/keylog.txt'
    data = urllib.request.urlopen( "file:keylog.txt" ).read().decode("ASCII")
    ruleDict= makePairs( data.splitlines() )
    #print ruleDict
    return "".join( list( topoSort(ruleDict)) )

# Confirm the answer.

def confirm(ans):
    assert ans == '73162890', "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans=answer()
    confirm( ans )
    print( "The shortest possible secret passcode of unknown length from the given file:", ans )