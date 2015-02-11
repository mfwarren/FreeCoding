#!/usr/bin/env python3
# imports go here
import atexit

#
# Free Coding session for 2015-02-10
# Written by Matt Warren
#


def clean_up():
    print("CLEANING UP")


@atexit.register
def done():
    print("DONE")

if __name__ == '__main__':
    atexit.register(clean_up)
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
