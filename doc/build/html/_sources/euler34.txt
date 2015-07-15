..  #!/usr/bin/env python3

Digit factorials
=================

Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

..  rubric:: Solution
..  py:module:: euler34
    :synopsis: Digit factorials

Question: what's the upper bound?  When they say "all numbers", what does that mean?

A number n has digits d0, d1, ... di each of which is in the set { 0, 1, 2, ... 9 }
di! is in the set F = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 }

n = sum(di!) for the digits of n.

n = 1*f0 + 1*f1 + 2*f2 + 6*f3 + 24*f4 + 120*f5 + 720*f6 + 5040*f7 + 40320*f8 + 362880*f9

Where fi is the frequency of a given digit di.

Use :py:func:`euler04.digits`.

::

  from euler04 import digits

Compute factorial of n. See :py:mod:`euler15` for another version of this.
Note that this version is limited by Python's stack size.

::

  def fact(a):
      """Factorial of a number, a.

      >>> from euler34 import fact
      >>> fact(9)
      362880
      """
      if a == 0: return 1
      return a*fact(a-1)

Find all curious numbers where the sum of digit factorial is the number.

::

  def curious( limit=999999 ):
      for i in range(3,limit+1):
          p = sum( map( fact, digits(i) ) )
          #print i, p
          if p == i:
              yield i

Test the components in this module.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      c= list( curious() )
      return sum(c)

Confirm the answer.

::

  def confirm(ans):
      assert 40730 == ans, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of all numbers which are equal to the sum of the factorial of their digits:", ans )