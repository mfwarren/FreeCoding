#!/usr/bin/env python3
# imports go here
import time
import sys
import random

#
# Free Coding session for 2015-04-15
# Written by Matt Warren
#

MESSAGE = "too busy coding tonight to write much"


def type_message(message):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05 + (random.random() / 10))
    print("")


if __name__ == '__main__':
    type_message(MESSAGE)
