..  #!/usr/bin/env python3

Powerful digit sum
==================

Problem 56

A googol (:math:`10^{100}`) is a massive number: one followed by one-hundred zeros; :math:`100^{100}`
is almost unimaginably large: one followed by two-hundred zeros. Despite their
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, :matH:`a^b`, where a, b < 100, what is the maximum
digital sum?

..  rubric:: Solution
..  py:module:: euler56
    :synopsis: Powerful digit sum

We'll use :py:func:`euler04.digits`.

::

  from euler04 import digits

Generate digit sums of a^b for a, b < 100.

::

  def digit_sum_gen():
      """
      >>> from euler56 import digit_sum_gen
      >>> max( digit_sum_gen() )
      (972, 99, 95)
      >>> sum(digits(99**95))
      972
      """
      for a in range(100):
          p= 1
          for b in range(100):
              s= sum(digits(p))
              yield s, a, b
              p *= a

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      s, a, b = max(digit_sum_gen())
      return s

Confirm the answer.

::

  def confirm( ans ):
      assert ans == 972, "{0!r} Incorrect".format(ans)

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm( ans )
      print( "The maximum digital sum of a**b for a, b < 100:", ans )