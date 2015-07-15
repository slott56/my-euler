..  #!/usr/bin/env python3

Special Pythagorean triplet
============================

Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

..  math::

    a^2 + b^2 = c^2

For example, :math:`3^2 + 4^2 = 9 + 16 = 25 = 5^2`.

There exists exactly one Pythagorean triplet for which :math:`a + b + c = 1000`.
Find the product :math:`abc`.

..  rubric:: Solution
..  py:module:: euler09
    :synopsis: Special Pythagorean triplet

Brute force calculation of triples a, b, c such that a+b+c=1000.

::

  def answer():
      for c in range( 1000 ):
          for b in range( 1, 1000-c ):
              a= 1000 - c - b
              if c > b > a:
                  assert a + b + c == 1000
                  if a*a + b*b == c*c:
                      #print a, b, c, a*a, b*b, c*c, a+b+c, a*b*c
                      return a*b*c

  def test():
      pass

Confirm the answer.

::

  def confirm():
      assert answer() == 31875000, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      confirm()
      print( "Product of pythogorean triplet summing to 1000:", answer() )