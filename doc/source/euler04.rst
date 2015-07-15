..  #!/usr/bin/env python3

Largest palindrome product
=============================

Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

..  rubric:: Solution
..  py:module:: euler04
    :synopsis: Largest palindrome product

..  py:function:: digits( n, b=10 )
    Break a number down into component digits and return a list object.

    :param n: a number to convert
    :param b: The base, default 10
    :returns: list of digits

::

  def digits( n, b=10 ):
      """Convert n to a sequence of digits."""
      d= []
      while n != 0:
          d.insert( 0, n % b )
          n = n // b
      return d

Test a number to see if it's a palindrome.

..  py:function:: palindrome( n, b=10 )
    Is the number a polindrome?

    :param n: A number
    :param b: base, default=10

::

  def palindrome( n, b=10 ):
      """True if the digits of n are a palindrome.

      >>> from euler04 import palindrome
      >>> palindrome(9009)
      True
      >>> palindrome(9008)
      False
      """
      d= digits(n, b)
      return d == d[::-1]

Generate all pairs of numbers, a and b, in the given range;
If the product is palindromic, yield that. We can use
explicit loops and an if statement.

Runtime 0.002

::

  def palInRange( low, high ):
      """Iterator over all palindroms which are products
      of two values in the given range.

      >>> from euler04 import palInRange
      >>> list( palInRange(10,100) ) # doctest: +ELLIPSIS
      [9009, ..., 121]
      """
      for i in range(high,low,-1):
          for j in range(high,i-1,-1):
              #print i,j,i*j
              if palindrome(i*j):
                  yield i*j

Generate all pairs of numbers, a and b, in the given range;
If the product is palindromic, yield that. We can use
two generator expressions to provide an iterable.

Runtime 0.010

::

  def palInRange2( low, high ):
      """Iterator over all palindroms which are products
      of two values in the given range.

      >>> from euler04 import palInRange2
      >>> list( palInRange2(10,100) ) # doctest: +ELLIPSIS
      [9009, ..., 121]
      """
      products = ( i*j for i in range(high,low,-1) for j in range(high,i-1,-1) )
      return ( n for n in products if palindrome(n) )

Locate the biggest Palindrome with the given number
of digits.

::

  def bigPal( digits ):
      """The largest Palindrome using numbers with the
      required number of digits. Slow version, using max.

      :math:`10^{d-1} <= n < 10{d}`

      >>> from euler04 import bigPal
      >>> bigPal(2)
      9009
      """
      return max( palInRange( 10**(digits-1), 10**digits ) )

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      return bigPal(3)

Confirm the answer.

::

  def confirm(ans):
      assert ans == 906609, "{0!r} Incorrect".format(ans)

Compare performace of the :py:func:`palInRange` and :py:func:`palInRange2` functions.

::

  def compare_timing():
      import timeit
      print( "palInRange", timeit.timeit( "palInRange(10,100)", "from euler04 import palInRange", number=10000) )
      print( "palInRange2", timeit.timeit( "palInRange2(10,100)", "from euler04 import palInRange2", number=10000) )

Create some the output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The largest palindrome made from the product of two 3-digit numbers:", ans )
      #compare_timing()