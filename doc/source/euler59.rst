..  #!/usr/bin/env python3

XOR decryption
==============

Problem 59

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method
is to use a password as a key. If the password is shorter than the message,
which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case
characters. Using `cipher1.txt <http://projecteuler.net/project/cipher1.txt>`_ (right click and 'Save Link/Target As...'), a file
containing the encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of the ASCII
values in the original text.


..  rubric:: Solution
..  py:module:: euler59
    :synopsis: XOR decryption

::

  import urllib.request
  from string import ascii_lowercase, punctuation, whitespace
  from collections import defaultdict
  import re

Implementation of :py:class:`collections.Counter`, using defaultdict.
Computes the frequency table of characters.

::

  def char_freq( message ):
      """
      >>> from euler59 import char_freq
      >>> cf= char_freq( "The quick brown fox jumped over the lazy dog." )
      >>> cf[:5]
      [('o', 4), ('e', 4), ('u', 2), ('t', 2), ('r', 2)]
      """
      fq= defaultdict(int)
      for c in message:
          cl= c.lower()
          if cl in ascii_lowercase:
              fq[cl] += 1
      common_chars= sorted( fq.items(), key=lambda x:(x[1],x[0]), reverse=True )
      return common_chars

Given a frequency table of characters,
how well do the top 5 characters match the top 12 in English?

Here are the top 12 most commonly-used characters in English.
Use NLTK for a more accurate list.

::

  top_char = { 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u'}
  def english_chars( freq_table ):
      """Top 5 actual out of expected top 12?

      >>> from euler59 import char_freq, english_chars
      >>> cf= char_freq( "the quick brown fox jumped over the lazy dog" )
      >>> english_chars( cf )
      True
      """
      return all( [ ch in top_char for ch, _ in freq_table[:5] ] )

Implementation of :py:class:`collections.Counter`, using defaultdict.
Computes the frequency table of words.

::

  def word_freq( message ):
      """
      >>> from euler59 import word_freq
      >>> wf= word_freq( "the quick brown fox jumped over the lazy dog" )
      >>> wf[0]
      ('the', 2)
      """
      fq= defaultdict(int)
      for w in message.split():
          fq[w.lower()] += 1
      common_words= sorted( fq.items(), key=lambda x:x[1], reverse=True )
      return common_words

Given a frequency table of words,
how well does the top word match the top word in English?

Top most commonly-used word(s) in English.
Use NLTK for a more accurate list.

::

  top_word = {"the"}

  def english_words( freq_table ):
      """
      >>> from euler59 import word_freq, english_words
      >>> wf= word_freq( "the quick brown fox jumped over the lazy dog" )
      >>> english_words( wf )
      True
      """
      wd0, _ = freq_table[0]
      return wd0 == "the"

Implement an xor-based decode of a message using a key.

Can also be :samp:`zip( message, key*(len(message)/len(key)) )`

::

  def xor_decode( message, key ):
      """
      >>> from euler59 import xor_decode
      >>> xor_decode( map(ord,['A']), [42] )
      [107]
      >>> list(map(chr,xor_decode( [107], [42] )))
      ['A']
      """
      len_key= len(key)
      return [ char ^ key[p%len_key] for p, char in enumerate(message) ]

Generate all possible 3-character keys.

::

  def genKey():
      for k1 in ascii_lowercase[:]:
          for k2 in ascii_lowercase[:]:
              for k3 in ascii_lowercase[:]:
                  yield k1+k2+k3

Brute-force decoding. Check the character and word frequency
to see if the key gave us something that appears to be English.

::

  def brute_force( coded ):
      for key in genKey():
          keyOrd= list( map( ord, key ) )
          clear= "".join( map( chr, xor_decode( coded, keyOrd ) ) )
          cf= char_freq( clear )
          if english_chars( cf ):
              wf= word_freq( clear )
              if english_words(wf):
                  print( "Key", key )
                  print( "Clear Text", clear )
                  print( "Character Frequencies", cf[:12] )
                  print( "Word Frequencies", wf[:12] )
                  print()
                  return clear

Test the module components.

::

  def test():
      import doctest
      doctest.testmod(verbose=0)

Compute the answer.

::

  def answer():
      # "http://projecteuler.net/project/cipher1.txt"
      with urllib.request.urlopen("file:cipher1.txt") as doc:
          coded= list( map( int, doc.read().decode("ascii").split(',') ) )
      #print( coded )
      clear= brute_force( coded )
      return sum( map( ord, clear ) )

  def confirm( ans ):
      assert 107359 == ans, "{0!r} Incorrect".format(ans)

  if __name__ == "__main__":
      test()
      ans= answer()
      confirm(ans)
      print( "The sum of the ASCII values in the original text:", ans )