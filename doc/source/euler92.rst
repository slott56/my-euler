..  #!/usr/bin/env python3

Square digit chains
===================

Problem 92

A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

    44 → 32 → 13 → 10 → 1 → 1

    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?

..  rubric:: Solution
..  py:module:: euler92
    :synopsis: Square digit chains

Use :py:func:`euler62.digits`, the version that generates the digits
rather than the other versions.
:py:func:`euler04.digits` creates a list;  :py:func:`euler51.digits` creates a tuple.

::

  from euler62 import digits
  import array
  import time

  class Chain1:
      """
      Slower than Chain2.

      >>> c= Chain1()
      >>> c.chain(44)
      1
      >>> c.chain(85)
      89
      """
      def __init__( self ):
          self.memoized = { 1:1, 89:89 }

      def _chain( self, n ):
          while n not in self.memoized:
              n= sum( d*d for d in digits(n) )
          return self.memoized[n]

      def chain( self, n ):
          if n not in self.memoized:
              self.memoized[n]= self._chain(n)
          return self.memoized[n]

  class Chain2( Chain1 ):
      """34 seconds total.

      >>> c= Chain2()
      >>> c.chain(44)
      1
      >>> c.chain(85)
      89
      """
      def _chain( self, n ):
          t= n
          visited= set()
          while t not in self.memoized:
              t= sum( d*d for d in digits(t) )
              visited.add(t)
          # Set all the numbers in this chain to point to the same result
          for u in visited:
              self.memoized[u]= self.memoized[t]
          return self.memoized[t]

  class Chain3( Chain1 ):
      """About the same as Chain2.

      >>> c= Chain3()
      >>> c.chain(44)
      1
      >>> c.chain(85)
      89
      """
      def __init__( self, size=10000000 ):
          self.memoized= array.array('b',size*[0])
          self.memoized[1]= 1
          self.memoized[89]= 89

      def _chain( self, n ):
          while self.memoized[n] == 0:
              n= sum( d*d for d in digits(n) )
          return self.memoized[n]

      def chain( self, n ):
          if self.memoized[n] == 0:
              self.memoized[n]= self._chain(n)
          return self.memoized[n]

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Create the answer.

::

  def answer():
      start= time.perf_counter()
      count= { 1: 0, 89: 0 }
      c= Chain2()
      for i in range(1,10000000):
          count[ c.chain(i) ] += 1
      run= time.perf_counter()-start
      # print( c.__class__.__name__, run )
      return count[89]

Confirm the answer.

::

  def confirm( ans ):
      assert ans == 8581146, "{0!r} Incorrect".format(ans)

Compare the performance of Chain1, Chain2 and Chain3.

::

  def compare_timing():
      import timeit
      print( "Chain1", timeit.timeit( "[c.chain(i) for i in range(1,10000)]", "from euler92 import Chain1; c=Chain1()", number=1000) )
      print( "Chain2", timeit.timeit( "[c.chain(i) for i in range(1,10000)]", "from euler92 import Chain2; c=Chain2()", number=1000) )
      print( "Chain3", timeit.timeit( "[c.chain(i) for i in range(1,10000)]", "from euler92 import Chain3; c=Chain3()", number=1000) )

Create some output.

::

  if __name__ == "__main__":
      test()
      compare_timing()
      ans= answer()
      confirm(ans)
      print( "The count of chains with starting numbers below ten million will arrive at 89:", ans )