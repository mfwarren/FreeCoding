#!/usr/bin/env python3
# imports go here
import sys
import time
import multiprocessing

#
# Free Coding session for 2015-04-24
# Written by Matt Warren
#

DELAY = 0.1
DISPLAY = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁']


def spinner(before='', after=''):
    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY)
        msg = before + DISPLAY[pos] + after
        sys.stdout.write(msg)
        sys.stdout.flush()
        sys.stdout.write('\x08' * len(msg))
        time.sleep(DELAY)


def long_computation():
    time.sleep(5)


if __name__ == '__main__':
    spinner = multiprocessing.Process(None, spinner, args=('Please wait ... ', ''))
    spinner.start()
    try:
        long_computation()
        print("complete")
    finally:
        spinner.terminate()
