..  #!/usr/bin/env python3

Circular primes
================

Problem 35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

..  rubric:: Solution
..  py:module:: euler35
    :synopsis: Circular primes

Include :py:func:`euler03.isprime` and :py:func:`euler04.digits`.

::

  from euler03 import isprime
  from euler04 import digits

Create a number from a sequence of digits.

..  py:function:: number(digits)
    Convert a sequence of digits to a number.

    :param digits: a sequence of digit values.
    :returns: integer value

::

  def number( digs ):
      n= 0
      for d in digs:
          n = 10*n + d
      return n

Iterate over all rotations of a number

::

  def rotations( d ):
      for s in range(len(d)):
          yield d[s:]+d[:s]

Find a set of all circular primes

::

  def circularPrimes( limit ):
      """
      >>> from euler35 import circularPrimes
      >>> cp100= circularPrimes( 100 )
      >>> len(cp100)
      13
      >>> sorted( set( cp100 ) )
      [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
      """
      cp= set()
      for n in range(2,limit):
          if isprime(n) and n not in cp:
              rs= [ number(r) for r in rotations( digits(n) ) ]
              circular= all( map( isprime, rs ) )
              if circular:
                  for r in rs:
                      cp.add(r)
      return cp

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      cp1m= circularPrimes( 1000000)
      return len(cp1m)

Confirm the answer.

::

  def confirm(answer):
      assert 55 == answer, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The number of circular primes below one million:", ans )