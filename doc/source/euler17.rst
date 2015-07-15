..  #!/usr/bin/env python3

Number letter counts
=====================

Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.

..  rubric:: Solution
..  py:module:: euler17
    :synopsis: Number letter counts

Our lexicon

::

  numbers = {
      1: "one", 2: "two", 3 : "three", 4:"four",  5: "five",
      6:"six", 7:"seven", 8:"eight", 9:"nine" }
  tens = {
      2:"twenty", 3:"thirty", 4:"forty", 5:"fifty",
      6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety" }
  teens = {
      10:"ten", 11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
      16: "sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" }

Create English words for numbers.

::

  def english( n ):
      """English for a number.

      >>> from euler17 import english
      >>> english(1)
      'one'
      >>> english(2)
      'two'
      >>> english(3)
      'three'
      >>> english(4)
      'four'
      >>> english(5)
      'five'
      >>> english(6)
      'six'
      >>> english(7)
      'seven'
      >>> english(8)
      'eight'
      >>> english(9)
      'nine'
      >>> english(10)
      'ten'
      >>> english(11)
      'eleven'
      >>> english(12)
      'twelve'
      >>> english(13)
      'thirteen'
      >>> english(14)
      'fourteen'
      >>> english(15)
      'fifteen'
      >>> english(16)
      'sixteen'
      >>> english(17)
      'seventeen'
      >>> english(18)
      'eighteen'
      >>> english(19)
      'nineteen'
      >>> english(20)
      'twenty'
      >>> english(99)
      'ninety-nine'
      >>> english(100)
      'one hundred'
      >>> english(101)
      'one hundred and one'
      >>> english(990)
      'nine hundred and ninety'
      >>> english(991)
      'nine hundred and ninety-one'
      >>> english(999)
      'nine hundred and ninety-nine'
      >>> english(1000)
      'one thousand'
      """
      words = []
      if n >= 1000:
          n4= n // 1000
          words.append( numbers[n4] )
          words.append( "thousand" )
          n = n % 1000
      if n >= 100:
          n3= n // 100
          words.append( numbers[n3] )
          words.append( "hundred" )
          n = n % 100
      if len(words) > 0 and n != 0:
          words.append( "and" )
      if n >= 20:
          n2, n3 = divmod( n, 10 )
          if n3 == 0:
              words.append( tens[n2] )
          else:
              words.append( tens[n2] + "-" + numbers[n%10] )
      elif n >= 10:
          words.append( teens[n] )
      elif n > 0:
          words.append( numbers[n] )
      else:
          assert n == 0
      return " ".join( words )

Count letters in a phrase after removing spaces and hyphens.

::

  def letters( text ):
      """Strip spaces and hyphens, and count letters.

      >>> from euler17 import english, letters
      >>> e342= english(342)
      >>> e342
      'three hundred and forty-two'
      >>> letters(e342)
      23
      >>> e115= english(115)
      >>> e115
      'one hundred and fifteen'
      >>> letters(e115)
      20
      """
      return len(text.replace('-','').replace(' ',''))

Demonstrate :py:func:`english` function.

::

  def demo():
      """Show first 20 numbers and 990 to 1001 to create bulk unit test cases."""
      for i in range(1, 21):
          print( ">>> english({0})\n{1!r}".format( i, english(i) ) )

      for i in range(990,1001):
          print( ">>> english({0})\n{1!r}".format( i, english(i) ) )

Test module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
     return sum( letters(english(i)) for i in range(1, 1001) )

Confirm the answer.

::

  def confirm(ans):
      assert ans == 21124, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The number of letters used to write"
          " all the numbers from 1 to 1000 inclusive:", ans )