#!/usr/bin/env python3
# imports go here
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from threading import Thread

#
# Free Coding session for 2015-02-07
# Written by Matt Warren
#


def run_server():
    server = SimpleXMLRPCServer(('localhost', 9000))
    server.register_function(pow)
    server.register_function(lambda x, y: x+y, 'add')
    server.register_multicall_functions()
    server.serve_forever()


def call_server():
    s = xmlrpc.client.ServerProxy('http://localhost:9000')
    x = 2
    while True:
        x = x + 1
        print(s.pow(2, x))

t = Thread(target=run_server)
t.start()
t2 = Thread(target=call_server)
t2.start()
