#!/usr/bin/env python3
# imports go here
import itertools
import random

from flask import Flask
from flask.ext.script import Manager
from flask.ext.restful import Api, Resource

#
# Free Coding session for 2015-01-10
# Written by Matt Warren
#


class Card:
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    FACES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def serialize(self):
        return {
            'suit': self.SUITS[self.suit],
            'face': self.FACES[self.face]
        }

    def __repr__(self):
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

    def get_card(self):
        return self.deck.pop()


app = Flask(__name__)
api = Api(app)
manager = Manager(app)


class CardAPI(Resource):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def get(self):
        return self.deck.get_card().serialize()

api.add_resource(CardAPI, '/')

if __name__ == '__main__':
    manager.run()
