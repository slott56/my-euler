..  #!/usr/bin/env python3

Largest prime factor
=======================

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

..  rubric:: Solution
..  py:module:: euler03
    :synopsis: Largest prime factor

::

  import math

A simple primality test. Would benefit from memoization.

..  py:function:: isprime(n)
    Is n prime?

    :param n: an integer
    :returns: True if n is prime.

::

  def isprime( n ):
      """Is n prime?

      >>> from euler03 import isprime
      >>> isprime(2)
      True
      >>> isprime(4)
      False
      """
      if n < 2: return False
      for i in range(2,1+int(math.sqrt(n))):
          if n % i == 0:
              return False
      return True

A simple, brute force, iterative search for the largest
factor which is also prime.

::

  def largestPrime(n):
      """Largest prime factor of n.

      >>> from euler03 import largestPrime
      >>> largestPrime(13195)
      29
      """
      f= int(math.sqrt(n))+1
      while n % f != 0 or not isprime(f):
          f= f-1
      return f

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the requested largest prime.

::

  def answer():
      return largestPrime(600851475143)

Confirm the answer.

::

  def confirm():
      assert answer() == 6857, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      confirm()
      print( "The largest prime factor of the number 600851475143:", answer() )
