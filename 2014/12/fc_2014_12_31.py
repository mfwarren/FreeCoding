#!/usr/bin/env python3
# imports go here
import asyncio
import datetime
# import os
import signal
import functools
from socket import socketpair

#
# Free Coding session for 2014-12-31
# Written by Matt Warren
#


def hello(loop):
    print("Hello")
    loop.stop()

loop = asyncio.get_event_loop()

loop.call_soon(hello, loop)
print('first')

loop.run_forever()
# loop.close()


def display_time(end_time, loop):
    print(datetime.datetime.now())
    if loop.time() + 1 < end_time:
        loop.call_later(1, display_time, end_time, loop)
    else:
        loop.stop()

end_time = loop.time() + 5
loop.call_soon(display_time, end_time, loop)

loop.run_forever()


rsock, wsock = socketpair()


def reader():
    data = rsock.recv(100)
    print("Got:", data.decode())
    loop.remove_reader(rsock)
    loop.stop()

loop.add_reader(rsock, reader)

loop.call_soon(wsock.send, 'abc'.encode())

loop.run_forever()

rsock.close()
wsock.close()


def ask_exit(signame):
    loop.stop()

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame), functools.partial(ask_exit, signame))

print("press CTRL+C to exit")

try:
    loop.run_forever()
except:
    pass
finally:
    loop.close()
