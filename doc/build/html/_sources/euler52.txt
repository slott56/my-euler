..  #!/usr/bin/env python3

Permuted multiples
==================

Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

..  rubric:: Solution
..  py:module:: euler52
    :synopsis: Permuted multiples

We'll use :py:func:`euler04.digits`.

::

  from euler04 import digits

We'll determine if two numbers, represented as digit tuples,
are permutations of each other.

..  py:function:: isPermutation( a, b )
    Are the two sequences permutations of each other?

    :param a: sequence
    :param b: sequence
    :returns: True of they're permutations of each other.

::

  def isPermutation( a, b ):
      """Is sequence *a* a permutation of sequence *b*?

      >>> from euler52 import isPermutation
      >>> n= 125874
      >>> isPermutation( digits(n), digits(2*n) )
      True
      >>> isPermutation( digits(n), digits(3*n) )
      True
      """
      return sorted(a) == sorted(b)

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=1)

Compute the answer.

::

  def answer():
      for i in range(1,1000000000):
          di= digits(i)
          p = [ isPermutation( di, digits(k*i) ) for k in range(2,7) ]
          if all(p):
              return i

Confirm the answer.

::

  def confirm(answer):
      assert answer == 142857, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      a= answer()
      confirm(a)
      print( "The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
          " the same digits:", a )