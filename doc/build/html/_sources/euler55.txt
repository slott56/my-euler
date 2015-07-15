..  #!/usr/bin/env python3

Lychrel numbers
===============

Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

    349 + 943 = 1292,

    1292 + 2921 = 4213

    4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number. Due to the theoretical
nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition you are given that
for every number below ten-thousand, it will either (i) become a palindrome in
less than fifty iterations, or, (ii) no one, with all the computing power that
exists, has managed so far to map it to a palindrome. In fact, 10677 is the
first number to be shown to require over fifty iterations before producing a
palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

..  rubric:: Solution
..  py:module:: euler55
    :synopsis: Lychrel numbers

Some handy functions we might need: :py:func:`euler04.palindrome`,
:py:func:`euler04.digits`, and :py:func:`euler35.number`.

::

  from euler04 import palindrome, digits
  from euler35 import number

Reverse the digits and add to the original number.

::

  def reverseAndAdd( n ):
      """
      >>> from euler55 import reverseAndAdd
      >>> from euler04 import palindrome
      >>> reverseAndAdd(47)
      121
      >>> palindrome( reverseAndAdd(47) )
      True
      >>> reverseAndAdd( reverseAndAdd( reverseAndAdd( 349 ) ) )
      7337
      >>> palindrome( reverseAndAdd( reverseAndAdd( reverseAndAdd( 349 ) ) ) )
      True
      """
      d = digits(n)
      d.reverse()
      return n + number(d)

Lychrel number within a given number of steps?

::

  def lychrel( n, limit=50 ):
      """
      >>> from euler55 import lychrel
      >>> lychrel(10677)
      True
      >>> lychrel(10677,limit=53)
      False
      >>> lychrel(4994)
      True
      """
      n= reverseAndAdd( n )
      for count in range(limit):
          if palindrome(n): return False
          n= reverseAndAdd( n )
      return True

Generate Lychrel numbers up to 10,000

::

  def lychrel_gen():
      for i in range(10000):
          if lychrel(i):
              yield i

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

      assert lychrel(10677)
      assert not lychrel(10677,limit=53)
      assert lychrel(4994)

Compute the answer.

::

  def answer():
      return len( list( lychrel_gen() ) )

Confirm the answer

::

  def confirm(ans):
      assert ans == 249, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The number of Lychrel numbers are there below ten-thousand:", ans )