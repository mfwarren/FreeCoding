#!/usr/bin/env python3
# imports go here
from xmlrpc.server import SimpleXMLRPCServer

#
# Free Coding session for 2015-02-05
# Written by Matt Warren
#

server = SimpleXMLRPCServer(('localhost', 9000))
server.register_function(pow)
server.register_function(lambda x, y: x+y, 'add')
server.register_multicall_functions()
server.serve_forever()


"""
>>> import xmlrpc.client
>>> s = xmlrpc.client.ServerProxy('http://localhost:9000')
>>> s.pow(2,3)
8
>>> s.add(4,2)
6
"""
