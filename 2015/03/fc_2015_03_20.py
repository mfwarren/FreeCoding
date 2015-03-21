#!/usr/bin/env python3
# imports go here
import aiohttp
import asyncio

#
# Free Coding session for 2015-03-20
# Written by Matt Warren
#

sem = asyncio.Semaphore(5)


@asyncio.coroutine
def get(url):
    with (yield from sem):
        response = yield from aiohttp.request('GET', url)
        return (yield from response.read_and_close())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(get('http://mattwarren.co'))
    print(val)
