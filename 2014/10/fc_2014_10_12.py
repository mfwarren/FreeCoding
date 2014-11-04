#!/usr/bin/env python
#imports go here
import itertools
import random

#
# Free Coding session for 2014-10-12
# Written by Matt Warren
#

class Card:
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    FACES = [2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return "%s of %s" % (self.FACES[self.face], self.SUITS[self.suit])

class Deck:
    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        for i, j in itertools.product(range(13), range(4)):
            self.deck.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.deck)

    def __iter__(self):
        while len(self.deck) > 0:
            yield self.deck.pop()

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    for card in deck:
        print card
