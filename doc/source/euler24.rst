..  #!/usr/bin/env python3

Lexicographic permutations
==========================

Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

..  rubric:: Solution
..  py:module:: euler24
    :synopsis: Lexicographic permutations

Let's start with a permutation generator. This uses a recursive algorithm
to enumate all permutations of a given set of values.

..  py:class:: Permutation
    Generates all permutations of a given sequence

::

  class Permutation:
      """An instance will generate permutations of a set of *n* single-digit
      string values.

      >>> from euler24 import Permutation
      >>> x = Permutation( '012' )
      >>> r3= list( x.strNextPerm() )
      >>> r3
      ['012', '021', '102', '120', '201', '210']

      >>> y = Permutation( [0, 1, 2] )
      >>> t3= list( y.nextPerm() )
      >>> t3 # doctest: +ELLIPSIS
      [[0, 1, 2], [0, 2, 1], ..., [2, 0, 1], [2, 1, 0]]
      """
      def __init__( self, values ):
          self.values= values
          self.n= len(values)
          self.state= self.n*[None]
      def nextPerm( self, p=0 ):
          for v in self.values:
              #print( "p= {0}, v={1!r}".format(p, v) )
              if v in self.state[:p]:
                  continue
              self.state[p]= v
              #print( self.state )
              if p+1 == self.n:
                  # State filled up: base case of recursion.
                  # Yield a shallow copy of the state.
                  # Yielding a tuple might be a better idea.
                  yield self.state[:]
              else:
                  # Recurse and generate more values.
                  for perm in self.nextPerm( p+1 ):
                      yield perm
      def strNextPerm( self ):
          for p in self.nextPerm():
              yield "".join( p )

Test the components in this module.

::

  def test():
      import doctest
      doctest.testmod(verbose=1)

Compute the answer.

::

  def answer():
      y = Permutation('0123456789') # 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
      for i,p in enumerate(y.nextPerm()):
          if i+1 == 1000000:
              return "".join( p )

Confirm the answer.

::

  def confirm(ans):
      assert "2783915460" == ans, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The millionth lexicographic permutation of the digits:", ans )