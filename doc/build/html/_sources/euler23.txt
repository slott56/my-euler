..  #!/usr/bin/env python3

Non-abundant sums
=================

Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number whose proper divisors are less than the number is called deficient and
a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

..  rubric:: Solution
..  py:module:: euler23
    :synopsis: Non-abundant sums

Use :py:func:`euler21.properDivisors` to compute the divisors.

::

  from euler21 import properDivisors

Generate abundant numbers by filtering a larger set of numbers.

::

  def abundant( source ):
      """Filter a source for abundant numbers.
      >>> from euler23 import abundant
      >>> list(abundant( (11, 12, 13) ))
      [12]
      """
      return ( i for i in source if sum(properDivisors(i)) > i )

Alternative filter function to pass abundant numbers
from a larger set of numbers.

::

  def abundant2( source ):
      """Filter a source for abundant numbers.
      >>> from euler23 import abundant2
      >>> list(abundant2( (11, 12, 13) ))
      [12]
      """
      for i in source:
          if sum(properDivisors(i)) > i:
              yield i

An generator which provides numbers which are not the sum of
two abundant numbers.

::

  def nonSum2Abundant( ):
      """Yield a sequence of numbers that are **not** the sum of two abundant numbers"""
      A_s = set( a for a in abundant(range(28124)) )

      def is_sum_2_abundant( n ):
          """Is n the sum of 2 numbers in the A_s set?"""
          for a in A_s:
              if n-a in A_s:
                  return True
          return False

      for n in range(28124):
          if is_sum_2_abundant( n ):
              pass
          else:
              yield n

Test the module components.

::

  def test():
      """
      from euler21 import properDivisors
      >>> p28= properDivisors(28)
      >>> p28
      [1, 2, 4, 7, 14]
      >>> sum(p28)
      28
      >>> p12= properDivisors(12)
      >>> p12
      [1, 2, 3, 4, 6]
      >>> sum(p12)
      16
      """
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      nonsum2 = nonSum2Abundant()
      return sum(nonsum2)

Confirm the answer.

::

  def confirm(ans):
      assert ans == 4179871, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of all the positive integers which cannot be written as the sum of"
      " two abundant numbers:", ans )
