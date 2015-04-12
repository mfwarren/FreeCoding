#!/usr/bin/env python3
# imports go here
from socket import *
from threading import Thread

#
# Free Coding session for 2015-04-11
# Written by Matt Warren
#

# process to provide fibonnaci numbers on socket.
# `nc localhost 25000` to test


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # prevent address already in use when restarting quickly
s.bind(('', 25000))
s.listen(5)


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)

while True:
    client, address = s.accept()
    print("connection", address)
    Thread(target=fib_handler, args=(client,), daemon=True).start()
