..  #!/usr/bin/env python3

10001st prime
=============================

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001\ :sup:`st` prime number?

..  rubric:: Solution
..  py:module:: euler07
    :synopsis: 10001st prime

An exception for composite numbers. We can raise this to break
out of a loop.

::

  class Composite( Exception ):
      pass

Seive of Eratosthones requires allocating some array of numbers and discarding
non-primes. How big should this array be? We could guess or experiment.

Python's list or set, however, allow us a flexible structure that allows us to
use a growing set of primes.

..  py:function:: primeGen()
    Iterator which emits prime numbers.

::

  def primeGen():
      """Generate prime numbers indefinitely.

      >>> from euler07 import primeGen
      >>> g= primeGen()
      >>> [ next(g) for _ in range(6) ]
      [2, 3, 5, 7, 11, 13]
      """
      yield 2
      primes= [2] # or set([2])
      n= 3
      limit= 2
      while True:
          try:
              for v in primes:
                  if v > limit: break
                  if n%v == 0:
                      raise Composite
              primes.append(n) # or primes.add(n)
              yield n
          except Composite:
              pass
          n= n + 2
          while limit*limit < n:
              limit += 1

..  py:function:: makePrimes( count )
    Generate a number of primes as a list object.

    :param count: number of primes to create
    :returns: list of primes of len(count)

::

  def makePrimes( count ):
      """Return count primes.

      >>> from euler07 import makePrimes
      >>> makePrimes(6)
      [2, 3, 5, 7, 11, 13]
      >>> makePrimes(1000)[-1]
      7919
      """
      g= primeGen()
      return [next(g) for _ in range(count)]

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the requested answer: 10,001\ :sup:`st` prime.

::

  def answer():
      return makePrimes(10001)[-1]

Confirm the answer.

::

  def confirm(ans):
      assert ans == 104743, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm( ans )
      print( "The 10001st prime number:", ans )
