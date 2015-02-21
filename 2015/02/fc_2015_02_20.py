#!/usr/bin/env python3
# imports go here
import threading
import time


#
# Free Coding session for 2015-02-20
# Written by Matt Warren
#


class MyThread(threading.Thread):

    def run(self):
        while True:
            print("HI There!")
            time.sleep(1)


if __name__ == '__main__':
    thread = MyThread()
    thread.start()
