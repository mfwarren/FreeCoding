#!/usr/bin/env python3
# imports go here
import os
import sys
import time

#
# Free Coding session for 2015-04-21
# Written by Matt Warren
#


def get_linux_terminal():
    width = os.popen('tput cols', 'r').readline()
    height = os.popen('tput lines', 'r').readline()

    return int(width), int(height)

message = "MATT"

printedMessage = ['','','','','','','']

characters = { ' ': [' ',
                     ' ',
                     ' ',
                     ' ',
                     ' ',
                     ' ',
                     ' '],
               'M': ['|\        /|',
                     '| \      / |',
                     '|  \    /  |',
                     '|   \  /   |',
                     '|    \/    |',
                     '|          |',
                     '|          |'],
               'A': ['      /\      ',
                     '     /  \     ',
                     '    /    \    ',
                     '   /======\   ',
                     '  /        \  ',
                     ' /          \ ',
                     '/            \\'],
               'T': ['___________',
                     '     |     ',
                     '     |     ',
                     '     |     ',
                     '     |     ',
                     '     |     ',
                     '     |     ']}

for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + '  ')

width, height = get_linux_terminal()
offset = width

while True:
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[7A\r')
    for row in range(7):
        sys.stdout.write(' ' * offset + printedMessage[row][max(0, offset*-1):width - offset])
        sys.stdout.write('\033[1B\r')
    offset -= 1
    if offset <= ((len(message) + 2) * 6) * -1:
        offset = width
    sys.stdout.flush()
    time.sleep(0.05)
