..  #!/usr/bin/env python3

Pandigital products
===================

Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in
more than one way so be sure to only include it once in your sum.

..  rubric:: Solution
..  py:module:: euler32
    :synopsis: Pandigital products

Use :py:class:`euler24.Permutation` to generate permutations.
Use :py:func:`euler35.number` to convert sequences of digits to proper numbers.

::

  from euler24 import Permutation
  from euler35 import number

Generate permutations of 9-digit numbers.

::

  def genPerms():
      """Create the 9! permutations of the digits 1-9.

      >>> from euler32 import genPerms
      >>> permList= list(genPerms())
      >>> len(permList) # 9! = 362880
      362880
      >>> permList[:2]
      [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9, 8]]
      >>> permList[-2:]
      [[9, 8, 7, 6, 5, 4, 3, 1, 2], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
      """
      permN= Permutation( range(1,10) ) # 1 to 9
      return permN.nextPerm()

  def panDigitProducts( permList ):
      """Take each permutation of digits and slice into 3 pieces.
      Check to see if each piece is a proper product.
      """
      for ai in range(1,9):
          for bi in range(ai):
              for perm in permList:
                  i, j, k = perm[:ai], perm[ai:ai+bi], perm[ai+bi:]
                  if number(i)*number(j) == number(k):
                      yield number(k)

Test the components in this module.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      permList= list( genPerms() )
      prodSet= set( panDigitProducts(permList) )
      return sum( list(prodSet) )

Confirm the answer.

::

  def confirm( ans ):
      assert ans == 45228, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of all products whose multiplicand/multiplier/product identity can"
          " be written as a 1 through 9 pandigital:", ans )