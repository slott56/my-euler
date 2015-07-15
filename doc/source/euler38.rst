..  #!/usr/bin/env python3

Pandigital multiples
=====================

Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

   192 × 1 = 192

   192 × 2 = 384

   192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?


..  rubric:: Solution
..  py:module:: euler38
    :synopsis: Pandigital multiples

We'll use :py:func:`euler04.digits` and :py:func:`euler35.number`.

::

  from euler04 import digits
  from euler35 import number

A test for being pan-digital. Zero's are excluded from the test.

::

  def pandigital( da, order=9 ):
      """All digits from 1 to order?

      >>> from euler38 import pandigital
      >>> pandigital( digits(192384576) )
      True
      >>> pandigital( digits(192384476) )
      False
      """
      if len(da) != 9: return False
      dSeen= (order+1)*[False]
      for d in da:
          dSeen[d]= True
      return all(dSeen[1:])

Compute a product concatenation from multiples of *n*. Stop when we
have a 9-digit number.

::

  def prodConcat( n ):
      """Create a 9-digit concatenaed product by successive multiplications
      of n by 1, 2, 3, ..., 9

      >>> from euler38 import prodConcat
      >>> prodConcat( 192 )
      [1, 9, 2, 3, 8, 4, 5, 7, 6]
      >>> prodConcat( 9 )
      [9, 1, 8, 2, 7, 3, 6, 4, 5]
      """
      seq= []
      for p in range(1,10):
          seq.extend( digits(n*p) )
          if len(seq) >= 9: break
      return seq

Generate all pan-digital numbers by starting within a range of 1,000,000.

::

  def genPanDigitalProdConcat():
      """Get the list of pandigital products.

      >>> from euler38 import genPanDigitalProdConcat
      >>> pdpc= list( genPanDigitalProdConcat() )
      >>> pdpc.sort()
      >>> pdpc # doctest: +ELLIPSIS
      [123456789, 192384576, 219438657, ..., 927318546, 932718654]
      """
      for i in range(1000000):
          seq= prodConcat(i)
          if pandigital(seq):
              yield number(seq)

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)
      assert pandigital( digits(192384576) )

Create the answer.

::

  def answer():
      return max( genPanDigitalProdConcat() )

  def confirm(ans):
      assert ans == 932718654, "{0!r} Incorrect".format(ans)

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The largest 1 to 9 pandigital 9-digit number that can be formed as the"
          " concatenated product of an integer with (1,2, ... , n) where n > 1:", ans )