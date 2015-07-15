..  #!/usr/bin/env python3

Amicable numbers
================

Problem 21

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

..  rubric:: Solution
..  py:module:: euler21
    :synopsis: Amicable numbers

A complete list of divisors is also part of :py:mod:`euler12`.
However, this list includes the number. This version
is just the "proper" divisors, excluding the number itself.

..  py:function:: properDivisors( x )
    Proper diviors of a number, including 1, excluding number itself.

    :param x: Number to get divisors of.

::

  def properDivisors( x ):
      """
      >>> from euler21 import properDivisors
      >>> properDivisors(220)
      [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
      >>> sum( properDivisors(220) )
      284
      >>> properDivisors(284)
      [1, 2, 4, 71, 142]
      >>> sum( properDivisors(284) )
      220
      """
      return [ i for i in range(1,x//2+1) if x%i == 0 ]

Test the components in the module.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      amicable= set()
      for a in range(10000):
          b= sum( properDivisors(a) )
          ax= sum( properDivisors(b) )
          if a == ax and a != b:
              #print "amicable", a, b
              amicable.add( a )
              amicable.add( b )
      return sum( amicable )

Confirm the answer.

::

  def confirm(ans):
      assert ans == 31626, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of all the amicable numbers under 10,000:", ans )
