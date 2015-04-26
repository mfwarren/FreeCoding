#!/usr/bin/env python3
# imports go here
import multiprocessing
import time

#
# Free Coding session for 2015-04-25
# Written by Matt Warren
#

def wait_for_event(e):
    print("waiting")
    e.wait()
    print("got event")


def wait_for_event_timeout(e, t):
    print("wait for timeout")
    e.wait(t)
    print("event timeout set", e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e,))
    w1.start()

    w2 = multiprocessing.Process(name='non-block', target=wait_for_event_timeout, args=(e, 2))
    w2.start()

    print('waiting before calling set')
    time.sleep(3)
    e.set()
    print('event set')
