#!/usr/bin/env python3
# imports go here
import multiprocessing
import time

#
# Free Coding session for 2015-03-03
# Written by Matt Warren
#

sem = multiprocessing.Semaphore()


def slow_function(count):
    time.sleep(1)
    print(count)


def slow_function2(count):
    with sem:
        time.sleep(1)
        print(count)


if __name__ == '__main__':

    print("start 1")
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=slow_function, args=(i,))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    print("start 2")
    for i in range(5):
        p = multiprocessing.Process(target=slow_function2, args=(i,))
        p.start()
