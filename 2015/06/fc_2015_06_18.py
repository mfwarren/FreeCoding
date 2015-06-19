#!/usr/bin/env python3
# imports go here
import sys
from random import randint
from time import sleep
#
# Free Coding session for 2015-06-18
# Written by Matt Warren
#
RED = '\033[41m'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'
END = '\033[0m'  # reset colors

def draw_blocks():
    while True:
        x, y = randint(1, 20), randint(1, 80)
        move_cursor = "\033[{};{}H".format(x, y)
        sys.stdout.write(SAVE_CURSOR + move_cursor + RED + ' ' + END + RESTORE_CURSOR)
        sys.stdout.flush()
        sleep(0.5)


if __name__ == '__main__':
    draw_blocks()
