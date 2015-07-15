..  #!/usr/bin/env python3

..  role:: hilight
    :class: red-text

..  default-role:: hilight

Spiral primes
=============

Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

..  parsed-literal::

    `37` 36 35 34 33 32 `31`
    38 `17` 16 15 14 `13` 30
    39 18  `5`  4  `3` 12 29
    40 19  6  1  2 11 28
    41 20  `7`  8  9 10 27
    42 21 22 23 24 25 26
    `43` 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

..  rubric:: Solution
..  py:module:: euler58
    :synopsis: Spiral primes

A handy function to create a spiral grid: :py:class:`euler28.SpiralGrid`.
Also, :py:func:`euler03.isprime`.

::

  from euler28 import SpiralGrid
  from euler03 import isprime

Our own prime test, which memoizes the various values to save
recomputing a known prime/non-prime result.

::

  memoized = {}
  def is_prime( n ):
      if n not in memoized:
          memoized[n]= isprime( n )
      return memoized[n]

Yield the diagonal values from the grid.

::

  def diagonals():
      sg= SpiralGrid().spiral(SpiralGrid.anti_clockwise)
      for v, pos in enumerate( sg ):
          x, y = pos
          if x == y:
              yield v+1
          elif x+y == 0:
              yield v+1
          else:
              pass

One attempt to provide the diagonals.

::

  def diagByOrderSlow( limit ):
      assert limit%2 == 1 and limit >= 3
      order= 3
      dList= []
      for d in diagonals():
          dList.append(d)
          if d == order*order:
              yield order, dList
              if order == limit:
                  return
              order += 2
              dList= []

A better attempt to emit the diagonals.

::

  def diagByOrder( limit ):
      """
      >>> from euler58 import diagByOrder
      >>> diag_iter= diagByOrder(7)
      >>> ord, d_list_1= next(diag_iter)
      >>> ord
      1
      >>> ord, d_list_3= next(diag_iter)
      >>> ord
      3
      >>> ord, d_list_5= next(diag_iter)
      >>> ord
      5
      >>> ord, d_list_7= next(diag_iter)
      >>> ord
      7
      >>> d_list_1 + d_list_3 + d_list_5 + d_list_7
      [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
      """
      yield 1, [1]
      for order in range(3,limit+2,2):
          corner= order*order
          yield order, [ corner-k*(order-1) for k in range(3,-1,-1) ]

Test the module components.

::

  def test():
      """
      >>> from euler58 import is_prime
      >>> d_list = [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
      >>> p_list= list(filter( is_prime, d_list ))
      >>> p_list
      [3, 5, 7, 13, 17, 31, 37, 43]
      >>> round(float(len(p_list))/len(d_list),2)
      0.62
      """
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      p_len= 0
      for order, next_d in diagByOrder(50001):
          next_p= list(filter( is_prime, next_d ))
          p_len += len(next_p)
          d_len = 2*(order-1)+1
          if order != 1 and p_len*10 < d_len:
              #print( order, float(p_len)/d_len )
              return order

Confirm the answer.

::

  def confirm(ans):
      assert ans == 26241, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The side length of the square spiral for which the ratio of primes along both"
          " diagonals first falls below 10%:", ans )