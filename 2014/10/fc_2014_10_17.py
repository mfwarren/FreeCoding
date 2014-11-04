#!/usr/bin/env python
#imports go here
import random
import itertools

#
# Free Coding session for 2014-10-17
# Written by Matt Warren
#

# doing a version of the card class but in a more functional style

SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
FACES = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

def print_card(suit, face):
    print "%s of %s" % (FACES[face], SUITS[suit])

if __name__=='__main__':
    cards = list(itertools.product(range(4),range(13)))
    #as far as I can tell there's no way to shuffle without converting to list
    random.shuffle(cards) #shuffle happens in place
    [print_card(*c) for c in cards]
