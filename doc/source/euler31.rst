..  #!/usr/bin/env python3

Coin sums
=========

Problem 31

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

..  rubric:: Solution
..  py:module:: euler31
    :synopsis: Coin sums

Our currency

::

  coinUniverse = (200, 100, 50, 20, 10, 5, 2, 1)

Filling in a coin toward a given subtotal.
This is a recursive generator. It adds a coin, and then
recursively works out coins for the remanining amounts,
if possible.

::

  def fillFrom( total, coinSet ):
      """Total is the amount to build, coinSet is an ordered
      sequence of coin values from largest to smallest.
    
      >>> from euler31 import fillFrom
      >>> list( fillFrom( 5, coinUniverse ) )
      [[5], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
      """
      if total == 0: return
      if len(coinSet) == 0: return
      count= total // coinSet[0]
      while count >= 0:
          remainder= total - count*coinSet[0]
          if remainder == 0:
              yield count*[coinSet[0]]
          else:
              for other in fillFrom( remainder, coinSet[1:] ):
                  yield count*[coinSet[0]] + other
          count = count - 1

Test the components of this module.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)
      for c in fillFrom( 100, coinUniverse ):
          assert sum(c) == 100

Compute the answer.

::

  def answer():
      return len(list(fillFrom( 200, coinUniverse )))

Confirm the answer.

::

  def confirm(ans):
      assert ans == 73682

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The number of different ways can £2 be made using any number of coins:", ans )