..  #!/usr/bin/env python3

Names scores
=============

Problem 22

Using `names.txt <http://projecteuler.net/project/names.txt>`_ (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938×53 = 49714.

What is the total of all the name scores in the file?

..  rubric:: Solution
..  py:module:: euler22
    :synopsis: Names scores

::

  import urllib.request
  from string import ascii_uppercase

Value of a name

::

  def value( name ):
      """
      >>> from euler22 import value
      >>> value("COLIN")
      53
      """
      chars= [ ascii_uppercase.index(c)+1 for c in name ]
      return sum( chars )

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      # "http://projecteuler.net/project/names.txt"
      namesText= urllib.request.urlopen( "file:names.txt" ).read().decode("ASCII")
      names= [ n.replace('"',"") for n in namesText.split(",") ]

      names.sort()
      values = ( (i+1)*value(name) for i, name in enumerate(names) )
      return sum(values)

Confirm the answer.

::

  def confirm():
      assert answer() == 871198282, "{0!r} Incorrect".format(ans)

Create some output.

::

  if __name__ == "__main__":
      test()
      confirm()
      print( "The total of all the name scores in the given file:", answer() )
