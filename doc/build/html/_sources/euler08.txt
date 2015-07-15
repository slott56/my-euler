..  #!/usr/bin/env python3

..  role:: hilight
   :class: red-text

..  default-role:: hilight

Largest product in a series
===============================

Problem 8

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

..  parsed-literal::

      73167176531330624919225119674426574742355349194934
      96983520312774506326239578318016984801869478851843
      85861560789112949495459501737958331952853208805511
      12540698747158523863050715693290963295227443043557
      66896648950445244523161731856403098711121722383113
      62229893423380308135336276614282806444486645238749
      30358907296290491560440772390713810515859307960866
      70172427121883998797908792274921901699720888093776
      65727333001053367881220235421809751254540594752243
      52584907711670556013604839586446706324415722155397
      53697817977846174064955149290862569321978468622482
      83972241375657056057490261407972968652414535100474
      821663704844031\ `9989`\ 0008895243450658541227588666881
      16427171479924442928230863465674813919123162824586
      17866458359124566529476545682848912883142607690042
      24219022671055626321111109370544217506941658960408
      07198403850962455444362981230987879927244284909188
      84580156166097919133875499200524063689912560717606
      05886116467109405077541002256983155200055935729725
      71636269561882670428252483600823257530420752963450

Older: Find the greatest product of five consecutive digits in the 1000-digit number.

Newer: Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

..  rubric:: Solution
..  py:module:: euler08
    :synopsis: Largest product in a series

::

  import euler05

Build a 1,000 character string from various lines.

::

  digits= "".join( """
  73167176531330624919225119674426574742355349194934
  96983520312774506326239578318016984801869478851843
  85861560789112949495459501737958331952853208805511
  12540698747158523863050715693290963295227443043557
  66896648950445244523161731856403098711121722383113
  62229893423380308135336276614282806444486645238749
  30358907296290491560440772390713810515859307960866
  70172427121883998797908792274921901699720888093776
  65727333001053367881220235421809751254540594752243
  52584907711670556013604839586446706324415722155397
  53697817977846174064955149290862569321978468622482
  83972241375657056057490261407972968652414535100474
  82166370484403199890008895243450658541227588666881
  16427171479924442928230863465674813919123162824586
  17866458359124566529476545682848912883142607690042
  24219022671055626321111109370544217506941658960408
  07198403850962455444362981230987879927244284909188
  84580156166097919133875499200524063689912560717606
  05886116467109405077541002256983155200055935729725
  71636269561882670428252483600823257530420752963450
  """.strip().split() )

  assert 1000 == len(digits)

Break the digit string into substrings of a given length.

::

  def digit_tuples( digits, n ):
      """Peel apart the digits and convert to substrings of length n.
      Map each substring to a tuple of integer values.

      >>> from euler08 import digit_tuples, digits
      >>> list( digit_tuples( digits, 5 ) ) # doctest: +ELLIPSIS
      [(7, 3, 1, 6, 7), ... (6, 3, 4, 5, 0)]
      >>> list( digit_tuples( digits, 13 ) ) # doctest: +ELLIPSIS
      [(7, 3, 1, 6, 7, 1, 7, 6, 5, 3, 1, 3, 3), ..., (0, 4, 2, 0, 7, 5, 2, 9, 6, 3, 4, 5, 0)]
      """
      combos = ( digits[i:i+n] for i in range(0,len(digits)-n+1) )
      return ( tuple(map(int,c)) for c in combos )

Compute products from each tuple in the sequence of digits.

::

  def max_prods( tuple_iter ):
      """Convert all digit lists into products, return just the max.

      >>> from euler08 import max_prods
      >>> max_prods( [(4,0,3,1), (9,9,8,9), (0,0,0,8)] )
      5832
      >>> max_prods( digit_tuples( digits, 4 ) )
      5832
      """
      prods = ( euler05.prod(t) for t in tuple_iter )
      return max(prods)

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)
      doctest.testmod( euler05, verbose=0)

Compute each of the two versions of the answer.

::

  def answer5():
      return max_prods( digit_tuples(digits, 5) )

  def answer13():
      return max_prods( digit_tuples(digits, 13) )

Confirm the old version.

::

  def confirm(ans5):
      assert ans5 == 40824, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans5= answer5()
      confirm(ans5)
      ans13= answer13()
      print( "The greatest product of five consecutive digits in the 1000-digit number:", ans5 )
      print( "The greatest product of thirteen consecutive digits in the 1000-digit number:", ans13 )