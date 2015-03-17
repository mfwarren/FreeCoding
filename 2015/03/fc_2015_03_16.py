#!/usr/bin/env python3
# imports go here
import json

#
# Free Coding session for 2015-03-16
# Written by Matt Warren
#


def decode(data, default={}):
    # subtle bug here:
    try:
        return json.loads(data)
    except:
        return default


if __name__ == '__main__':
    foo = decode('not json')
    foo['new'] = 'ha!'
    bar = decode('also not json')
    bar['what'] = 'what dictionary is it going into'

    assert foo is bar
