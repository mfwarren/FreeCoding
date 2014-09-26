#!/usr/bin/env python
import itertools
import random

class Card:
  SUITS = ['Spades', 'Diamonds', 'Hearts','Clubs']
  FACES = ['2', '3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
  def __init__(self, suit_num, face_num):
    self.suit = suit_num
    self.face = face_num

  def __str__(self):
    return "%s of %s" % (self.FACES[self.face], self.SUITS[self.suit])

class Deck:
  def __init__(self):
    self.deck = []
    self.build_deck()
    assert(len(self.deck) == 52)

  def build_deck(self):
    for i,j in itertools.product(range(4),range(13)):
      self.deck.append(Card(i,j))

  def shuffle(self):
    random.shuffle(self.deck)

  def draw_card(self):
    return self.deck.pop()

  def __iter__(self):
    while len(self.deck) > 0:
      yield self.draw_card()


if __name__=="__main__":
  deck = Deck()
  deck.shuffle()

  for card in deck:
    print card
