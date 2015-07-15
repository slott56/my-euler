..  #!/usr/bin/env python3

..  role:: hilight
   :class: red-text

..  default-role:: hilight

Number spiral diagonals
========================

Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

..  parsed-literal::

    `21` 22 23 24 `25`
    20  `7`  8  `9` 10
    19  6  `1`  2 11
    18  `5`  4  `3` 12
    `17` 16 15 14 `13`

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?

..  rubric:: Solution
..  py:module:: euler28
    :synopsis: Number spiral diagonals

..  py:class:: SpiralGrid
    Emits the indices required to populate the spiral grid.

    TThe spiral() method is an iterator over positions.
    The grid can be built from this sequence of (x,y) locations.


::

  class SpiralGrid:
      def __init__( self, n=None ):
          if n is not None:
              assert n % 2 == 1
              self.order= n
              self.offset= n//2
          else:
              self.order= -1 # will loop forever
              self.offset= 0
          self.x, self.y = 0, 0
      def right( self ):
          self.x += 1
      def down( self ):
          self.y += 1
      def left( self ):
          self.x -= 1
      def up( self ):
          self.y -= 1
      def move( self, direction, step ):
          for i in range(step):
              direction()
              yield self.x, self.y
      clockwise= 1
      anti_clockwise= 2
      def spiral( self, direction=clockwise ):
          if direction == self.clockwise:
              sequence = ( self.right, self.down, self.left, self.up )
          else:
              sequence = ( self.right, self.up, self.left, self.down )
          yield self.x+self.offset, self.y+self.offset
          step = 1
          while step != self.order:
              for d in sequence[:2]:
                  for x,y in self.move( d, step ):
                      yield x+self.offset, y+self.offset
              for d in sequence[2:]:
                  for x,y in self.move( d, step+1 ):
                      yield x+self.offset, y+self.offset
              step = step+2
          for x,y in self.move( self.right, step-1 ):
              yield x+self.offset, y+self.offset

Demonstrate that it does the right thing.

::

  def grid_display(order):
      """Test of SpiralGrid. Use the coordinate iterator
      to step through all x,y pairs and load a matrix.

      >>> from euler28 import grid_display
      >>> grid_display(5)
      [21, 22, 23, 24, 25]
      [20, 7, 8, 9, 10]
      [19, 6, 1, 2, 11]
      [18, 5, 4, 3, 12]
      [17, 16, 15, 14, 13]
      """
      mat= [ [0]*5 for i in range(5) ]
      x= SpiralGrid(order)
      for i,c in enumerate(x.spiral()):
          x,y = c
          mat[y][x]= i+1
      for y in range(5):
          print( mat[y] )

Sum the diagnanals of a spiral grid of order n

::

  def diagonal_sums(n):
      """Diagonal sums from a spiral grid of a given order.

      Note that the center must not be counted twice!

      >>> from euler28 import diagonal_sums
      >>> diagonal_sums(5)
      101
      """
      x= SpiralGrid(n)
      main= []
      sub= []
      for i,c in enumerate( x.spiral() ):
          if c[0] == c[1]:
              main.append( i+1 )
          if c[0] + c[1] == n-1 and c[0] != c[1]:
              sub.append( i+1 )
      #print( main, sum(main) )
      #print( sub, sum(sub) )
      return sum(main)+sum(sub)

Test the components in this module.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)
      #grid_display(5)

Compute the answer.

::

  def answer():
     return diagonal_sums(1001)

Confirm the answer.

::

  def confirm(ans):
      assert 669171001 == ans, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of both diagonals in a 1001 by 1001 spiral:", ans )