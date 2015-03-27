#!/usr/bin/env python3
# imports go here
import asyncio
import time
import random
#
# Free Coding session for 2015-03-26
# Written by Matt Warren
#


class ProducerConsumer(object):
    def __init__(self):
        self.queue = asyncio.Queue()
        self.producer_sem = asyncio.Semaphore()
        self.consumer_sem = asyncio.Semaphore()

    @asyncio.coroutine
    def post_data(self, data):
        with (yield from self.producer_sem):
            while True:
                yield from self.queue.put(data)
                yield from asyncio.sleep(0.5 + random.random())

    @asyncio.coroutine
    def read_data(self):
        with (yield from self.consumer_sem):
            while True:
                response = yield from self.queue.get()
                print(response)


if __name__ == '__main__':
    pc = ProducerConsumer()
    asyncio.Task(pc.read_data())
    asyncio.Task(pc.post_data("hi"))
    loop = asyncio.get_event_loop()
    loop.run_forever()
