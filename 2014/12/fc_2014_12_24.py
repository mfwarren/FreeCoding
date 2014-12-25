#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2014-12-24
# Written by Matt Warren
#


def print_tree():
    print('{:>21}#'.format(" "))
    padding = 20
    for i in range(0, 15):
        padding = padding - 1
        if i % 5 == 0:
            padding = padding + 2
        print(('{:>' + str(padding) + '}''{:>' + str(44-(padding*2)) + '}').format("#", "#"))
    print((' '*(padding-1))+("#"*((2*(padding+1))-1)))
    for i in range(0, 3):
        print(('{:>' + str(20) + '}''{:>' + str(44-(20*2)) + '}').format("#", "#"))
    print('{:>19}#####'.format(" "))

if __name__ == '__main__':
    print_tree()
