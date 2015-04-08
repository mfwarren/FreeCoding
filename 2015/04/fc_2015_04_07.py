#!/usr/bin/env python3
# imports go here
import threading
import time

#
# Free Coding session for 2015-04-07
# Written by Matt Warren
#


class Matt(threading.Thread):
    def __init__(self):
        super().__init__()
        self.will_stop = threading.Event()

    def stop(self):
        self.will_stop.set()

    def is_stopped(self):
        return self.will_stop.is_set()

    def run(self):
        print('starting')
        self.will_stop.wait()
        print('finished')

if __name__ == '__main__':
    m = Matt()
    m.start()

    assert not m.is_stopped()

    time.sleep(2)

    m.stop()
    m.join()
