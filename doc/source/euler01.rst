..  #!/usr/bin/env python3

Multiples of 3 and 5
=======================

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

..  rubric:: Solution

..  py:module:: euler01
    :synopsis: Multiples of 3 and 5

The approach is to create a set of numbers that's a union.
Let's do that literally.


::

  def answer1():
      """Use set(range(0,1000,3)) | set(range(0,1000,5)).
      Fast.
      """
      m3= range(0,1000,3)
      m5= range(0,1000,5)
      return sum(set(m3).union(set(m5)))

We can also do this with a loop and an if statement.

::

  def answer2():
      """Use an explicit loop and if statement.
      This is actually 8x slower than answer1().
      """
      sum= 0
      for i in range(1000):
          if i % 3 != 0 and i % 5 != 0:
              continue
          sum += i
      return sum

Confirm the answer.

::

  def confirm( ans ):
      assert ans == 233168, "{0!r} Incorrect".format(ans)

Compare performance of the :py:func:`answer1` and :py:func:`answer2` function2.

::

  def compare_timing():
      import timeit
      print( "answer1", timeit.timeit( "answer1()", "from euler01 import answer1", number=10000) )
      print( "answer2", timeit.timeit( "answer2()", "from euler01 import answer2", number=10000) )

Create some output.

::

  if __name__ == "__main__":
      ans= answer1()
      confirm(ans)
      ans= answer2()
      confirm(ans)
      print( "Sum of all the multiples of 3 or 5 below 1000:", ans )
      #compare_timing()