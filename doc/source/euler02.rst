..  #!/usr/bin/env python3

Even Fibonacci numbers
=======================

Problem 2

Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the
sequence which do not exceed four million.

..  rubric:: Solution
..  py:module: euler02
    :synopsis: Even Fibonacci numbers

Note that the sequence is always even - odd - odd...

odd (1) + even (2) => odd (3)

even (2) + odd (3) => odd (5)

odd (3) + odd (5) => even (8)

We're looking at sum( F(n*3) ) for integer n where F(n) < 4,000,000

F(n+3) = F(n+2) + F(n+1)

F(n+2) = F(n+1) + F(n)

F(n+1) = F(n) + F(n-1)

Doing a little algebra, we see this:

F(n+3) = F(n+1) + F(n) + F(n+1)

F(n+3) = F(n)+F(n-1) + F(n) + F(n)+F(n-1)

F(n+3) appears to be 4*F(n)+F(n-3)

::

  def evenFib( limit ):
      """
      Generate only the even Fibonacci numbers

      >>> from euler02 import evenFib
      >>> sum(evenFib(100))
      44
      """
      Fn= 2
      Fn3= 0
      while Fn <= limit:
          yield Fn
          Fn3, Fn = Fn, Fn*4+Fn3

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the result using the limit of 4,000,000.

::

  def answer():
      return sum(evenFib(4000000))

Confirm the answer.

::

  def confirm():
      assert answer() == 4613732, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      confirm()
      print( "Sum of all the even-valued terms in the "
            "sequence which do not exceed four million:", answer() )
