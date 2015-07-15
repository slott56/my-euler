#!/usr/bin/env python3

# Poker hands
# ===========

# Problem 54

# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#
# -   High Card: Highest value card.
# -   One Pair: Two cards of the same value.
# -   Two Pairs: Two different pairs.
# -   Three of a Kind: Three cards of the same value.
# -   Straight: All cards are consecutive values.
# -   Flush: All cards of the same suit.
# -   Full House: Three of a kind and a pair.
# -   Four of a Kind: Four cards of the same value.
# -   Straight Flush: All cards are consecutive values of same suit.
# -   Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
#
#     2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives
# (see example 1 below). But if two ranks tie, for example, both players
# have a pair of queens, then highest cards in each hand are compared (see
# example 4 below); if the highest cards tie then the next highest cards
# are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# ..  csv-table::
#     :header: Hand, Player 1, Player 2, Winner
#
#     1,"5H 5C 6S 7S KD; Pair of Fives",                     "2C 3S 8S 8D TD; Pair of Eights",     Player 2
#     2,"5D 8C 9S JS AC; Highest card Ace",                  "2C 5C 7D 8S QH; Highest card Queen", Player 1
#     3,"2D 9C AS AH AC; Three Aces",                        "3D 6D 7D TD QD; Flush with Diamonds", Player 2
#     4,"4D 6S 9H QH QC; Pair of Queens; Highest card Nine", "3D 6D 7H QD QS; Pair of Queens; Highest card Seven",      Player 1
#     5,"2H 2D 4C 4D 4S; Full House; With Three Fours",      "3C 3D 3S 9S 9D; Full House; with Three Threes",     Player 1
#
# The file, `poker.txt <http://projecteuler.net/project/poker.txt>`_, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a single
# space): the first five are Player 1's cards and the last five are Player
# 2's cards. You can assume that all hands are valid (no invalid
# characters or repeated cards), each player's hand is in no specific
# order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

# ..  rubric:: Solution
# ..  py:module:: euler54
#     :synopsis: Poker hands

import urllib.request
import collections
from pprint import pprint

# Card ranks: we'll use this to translate the input cards
# into more useful numeric orders for ranking.

rank_code = dict(
    ((str(i), i) for i in range(2,10)),
    T=10,
    J=11,
    Q=12,
    K=13,
    A=14
)

# A super-simple class for a playing card.

Card = collections.namedtuple( "Card", "rank,suit" )

# When we want to properly order a card, we'll extract
# the rank. This *should* be a method function or a
# property of the :py:class:`Card` class.

def order( card ):
    return card.rank

# A factory function to create a Card from a string.

def to_card( string ):
    assert len(string) == 2
    rank, suit = string
    return Card( rank_code[rank], suit )

# A factory function to create a hand of cards from a sequence of string
# card representations.

def to_hand( strings ):
    """Hand is a tuple of Card instances sorted from low to high."""
    assert len(strings) == 5
    hand= [to_card(c) for c in strings]
    hand.sort() # Ascending order by rank. hand[4] is high card.
    assert order(hand[4]) >= order(hand[0])
    return tuple(hand)

# Is this hand a flush?

def flush( hand ):
    return all( c.suit == hand[0].suit for c in hand )

# Is this hand a straight?

def straight( hand ):
    #print( "straight", tuple(c.rank-hand[0].rank for c in hand) )
    return tuple(c.rank-hand[0].rank for c in hand) == (0,1,2,3,4)

# A simple class to save the kinds of matching cards in a Hand.

Match = collections.namedtuple( "Match", "count,card" )

# An iterator which yields the Match instances found in a Hand.

def match_iter( hand ):
    fq, c0 = 1, hand[0]
    for c in hand[1:]:
        if c.rank == c0.rank:
            fq += 1
        else:
            yield Match( fq, c0 )
            fq, c0 = 1, c
    yield Match(fq, c0)

# The final list of Match instances, sorted.

def matches(hand):
    """A list of Match instances sorted
    from most frequent to least frequent."""
    return list(sorted(match_iter(hand), reverse=True))

# Create a numeric score to summarize the value of a hand.

def score_int( hand ):
    """
    Create numeric scores that includes the hand and one or two cards.

    High Card: Highest value card. 100*card
    One Pair: Two cards of the same value. 10000+100*card
    Two Pairs: Two different pairs. 20000+100*card+card
    Three of a Kind: Three cards of the same value. 30000+100*card
    Straight: All cards are consecutive values. 40000+100*card
    Flush: All cards of the same suit. 50000+100*card
    Full House: Three of a kind and a pair. 60000+100*card+card
    Four of a Kind: Four cards of the same value. 70000+100*card
    Straight Flush: All cards are consecutive values of same suit. 80000+100*card
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    """
    m = matches(hand)
    #print( m )
    #royal_flush -- a special case of straight flush.
    if flush(hand) and straight(hand) and hand[4].rank == 14:
        return 80000 + 100*order(hand[4])
    #straight_flush
    elif flush(hand) and straight(hand):
        return 80000 + 100*order(hand[4])
    #four_of_a_kind
    elif len(m) == 2 and m[0].count == 4:
        return 70000 + 100*order(m[0].card)
    #full_house
    elif len(m) == 2 and m[0].count == 3 and m[1].count == 2:
        return 60000 + 100*order(m[0].card) + order(m[1].card)
    #flush
    elif flush(hand):
        return 50000 + 100*order(hand[4])
    #straight
    elif straight(hand):
        return 40000 + 100*order(hand[4])
    #three_of_a_kind
    elif len(m) == 3 and m[0].count == 3:
        return 30000 + 100*order(m[0].card)
    #two_pair
    elif len(m) == 3 and m[0].count == 2 and m[1].count == 2:
        return 20000 + 100*order(m[0].card) + order(m[1].card)
    #one_pair
    elif len(m) == 4 and m[0].count == 2 and m[1].count == 1:
        return 10000 + 100*order(m[0].card) + order(m[1].card)
    # Simple high card. Is this adequate? We'll know if we get ties.
    else:
        return         100*order(hand[4]) # or 100*order(m[0].card)

# Create a scoring tuple: the numeric score and the
# one or two relevant ranks required to disambiguate ties
# in the numeric score.

def score_tuple( hand ):
    """Create score tuples of (number, rank, rank)

    High Card: Highest value card. (0,rank)
    One Pair: Two cards of the same value. (1,rank)
    Two Pairs: Two different pairs. (2,rank,rank)
    Three of a Kind: Three cards of the same value. (3,rank)
    Straight: All cards are consecutive values. (4,rank)
    Flush: All cards of the same suit. (5,rank)
    Full House: Three of a kind and a pair. (6,rank,rank)
    Four of a Kind: Four cards of the same value. (7,rank)
    Straight Flush: All cards are consecutive values of same suit. (8,rank)
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    >>> from euler54 import score_tuple, to_hand
    >>> score_tuple(to_hand("2C 4D 6H 8S TC".split()))
    (0, 10, 0)
    >>> score_tuple(to_hand("TD 4D 6H 8S TC".split()))
    (1, 10, 8)
    >>> score_tuple(to_hand("TD 8D 6H 8S TC".split()))
    (2, 10, 8)
    >>> score_tuple(to_hand("TD 8D TH 6S TC".split()))
    (3, 10, 0)
    >>> score_tuple(to_hand("TD 8D 9H 7S 6C".split()))
    (4, 10, 0)
    >>> score_tuple(to_hand("TD 8D 9D 6D 2D".split()))
    (5, 10, 0)
    >>> score_tuple(to_hand("TD TS 8S 8D TC".split()))
    (6, 10, 8)
    >>> score_tuple(to_hand("TD TS TC TH 8C".split()))
    (7, 10, 0)
    >>> score_tuple(to_hand("TD 6D 8D 7D 9D".split()))
    (8, 10, 0)
    """
    m = matches(hand)
    #print( m )
    #royal_flush -- a special case of straight flush.
    if flush(hand) and straight(hand) and hand[4].rank == 14:
        return (8, hand[4].rank, 0)
    #straight_flush
    elif flush(hand) and straight(hand):
        return (8, hand[4].rank, 0)
    #four_of_a_kind
    elif len(m) == 2 and m[0].count == 4:
        return (7, m[0].card.rank, 0)
    #full_house
    elif len(m) == 2 and m[0].count == 3 and m[1].count == 2:
        return (6, m[0].card.rank, m[1].card.rank)
    #flush
    elif flush(hand):
        return (5, hand[4].rank, 0)
    #straight
    elif straight(hand):
        return (4, hand[4].rank, 0)
    #three_of_a_kind
    elif len(m) == 3 and m[0].count == 3:
        return (3, m[0].card.rank, 0)
    #two_pair
    elif len(m) == 3 and m[0].count == 2 and m[1].count == 2:
        return (2, m[0].card.rank, m[1].card.rank)
    #one_pair
    elif len(m) == 4 and m[0].count == 2 and m[1].count == 1:
        return (1, m[0].card.rank, m[1].card.rank)
    # Simple high card. Is this adequate? We'll know if we get ties.
    else:
        return (0, hand[4].rank, 0) # or (0, m[0].card.rank, 0)

def score_hands():
    """
    >>> from euler54 import score_hands
    >>> outcome= score_hands()
    >>> outcome[1]
    376
    >>> outcome[2]
    624
    """
    #"http://projecteuler.net/project/poker.txt"
    poker_txt= urllib.request.urlopen( "file:poker.txt" ).read().decode("ASCII")
    outcome= collections.Counter()
    for line in poker_txt.splitlines():
        if not line: continue
        cards= line.split()
        assert len(cards) == 10
        h_1 = to_hand(cards[:5])
        h_2 = to_hand(cards[5:])
        s_1= score_tuple(h_1)
        s_2= score_tuple(h_2)
        assert s_1 != s_2, "Problem scoring {0!r} {1!r}".format(h_1,h_2)
        winner= 1 if s_1 > s_2 else 2
        # The most obscure case:
        # if s_1[:2] == s_2[:2]:
        #     print( "Close", cards[:5], s_1, cards[5:], s_2, winner )
        outcome[winner] += 1
        # Paranoid double check on two scoring systems.
        if score_int(h_1) > score_int(h_2) if winner == 1 else score_int(h_1) < score_int(h_2):
            pass
        else:
            print( "{!r} {!r} Player {:d}".format(cards[:5],cards[5:],winner) )
            print( s_1, ":", s_2 )
            print( score_int(h_1), score_int(h_2) )
            raise AssertionError( "Logic Problem" )
    return outcome

# Test the module components.

def test():
    """

    The most obscure case in the input file.

    >>> from euler54 import score_tuple, to_hand
    >>> s_1= score_tuple(to_hand(['6D', '7C', '5D', '5H', '3S']))
    >>> s_1
    (1, 5, 7)
    >>> s_2= score_tuple(to_hand(['5C', 'JC', '2H', '5S', '3D']))
    >>> s_2
    (1, 5, 11)
    >>> winner= 1 if s_1 > s_2 else 2
    >>> winner
    2
    """
    import doctest
    doctest.testmod(verbose=0)
    test_int()
    test_tuple()

def test_int():
    """
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights


2       5D 8C 9S JS AC	    2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen


3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds


4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven


5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes
    """
    cards= "5H 5C 6S 7S KD      2C 3S 8S 8D TD".split()
    h1, h2 = to_hand(cards[:5]), to_hand(cards[5:])
    s_h1, s_h2 = score_int(h1), score_int(h2)
    assert s_h1 == 10000+100*(5)+(13)
    assert s_h2 == 10000+100*(8)+(10)
    assert s_h1 < s_h2

    cards= "5D 8C 9S JS AC	    2C 5C 7D 8S QH".split()
    s_h1, s_h2 = score_int(to_hand(cards[:5])), score_int(to_hand(cards[5:]))
    assert s_h1 == 100*(14)
    assert s_h2 == 100*(12)
    assert s_h1 > s_h2

    cards= "2D 9C AS AH AC      3D 6D 7D TD QD".split()
    s_h1, s_h2 = score_int(to_hand(cards[:5])), score_int(to_hand(cards[5:]))
    #print( h1, "=", s_h1, ":", h2, "=", s_h2 )
    assert s_h1 == 30000+100*(14)
    assert s_h2 == 50000+100*(12)
    assert s_h1 < s_h2

    cards= "4D 6S 9H QH QC      3D 6D 7H QD QS".split()
    s_h1, s_h2 = score_int(to_hand(cards[:5])), score_int(to_hand(cards[5:]))
    assert s_h1 == 10000+100*(12)+(9)
    assert s_h2 == 10000+100*(12)+(7)
    assert s_h1 > s_h2

    cards= "2H 2D 4C 4D 4S      3C 3D 3S 9S 9D".split()
    s_h1, s_h2 = score_int(to_hand(cards[:5])), score_int(to_hand(cards[5:]))
    assert s_h1 == 60000+100*(4)+(2)
    assert s_h2 == 60000+100*(3)+(9)
    assert s_h1 > s_h2

def test_tuple():
    cards= "5H 5C 6S 7S KD      2C 3S 8S 8D TD".split()
    h1, h2 = to_hand(cards[:5]), to_hand(cards[5:])
    s_h1, s_h2 = score_tuple(h1), score_tuple(h2)
    assert s_h1 == (1,5,13)
    assert s_h2 == (1,8,10)
    assert s_h1 < s_h2

    cards= "5D 8C 9S JS AC	    2C 5C 7D 8S QH".split()
    s_h1, s_h2 = score_tuple(to_hand(cards[:5])), score_tuple(to_hand(cards[5:]))
    assert s_h1 == (0,14,0)
    assert s_h2 == (0,12,0)
    assert s_h1 > s_h2

    cards= "2D 9C AS AH AC      3D 6D 7D TD QD".split()
    s_h1, s_h2 = score_tuple(to_hand(cards[:5])), score_tuple(to_hand(cards[5:]))
    #print( h1, "=", s_h1, ":", h2, "=", s_h2 )
    assert s_h1 == (3,14,0)
    assert s_h2 == (5,12,0)
    assert s_h1 < s_h2

    cards= "4D 6S 9H QH QC      3D 6D 7H QD QS".split()
    s_h1, s_h2 = score_tuple(to_hand(cards[:5])), score_tuple(to_hand(cards[5:]))
    assert s_h1 == (1,12,9)
    assert s_h2 == (1,12,7)
    assert s_h1 > s_h2

    cards= "2H 2D 4C 4D 4S      3C 3D 3S 9S 9D".split()
    s_h1, s_h2 = score_tuple(to_hand(cards[:5])), score_tuple(to_hand(cards[5:]))
    assert s_h1 == (6,4,2)
    assert s_h2 == (6,3,9)
    assert s_h1 > s_h2

# Compute the answer.

def answer():
    outcome= score_hands()
    return outcome[1]

# Confirm the answer.

def confirm(ans):
    assert ans == 376, "{0!r} Incorrect".format(ans)

# Create some output.

if __name__ == "__main__":
    test()
    ans= answer()
    confirm(ans)
    print( "The number of hands player 1 wins:", ans )