#!/usr/bin/env python
#imports go here
from datetime import datetime
import time

#
# Free Coding session for 2014-10-15
# Written by Matt Warren
#

def follow(f):
    # f is an open file
    file = f.seek(0, 2) #seeks to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def cast(arr_of_dict, col, fn):
    for d in arr_of_dict:
        d[col] = fn(d[col])
        yield d

def parse(lines):
    tuples = (line.split(',') for line in lines)

    headings = ['id', 'name', 'value', 'created at']
    zipped_up = (dict(zip(headings, t) for t in tuples)
    zipped_up = cast(zipped_up, 'id', int)
    zipped_up = cast(zipped_up, 'value', int)
    zipped_up = cast(zipped_up, 'created at', lambda x: datetime.strptime(x, "%d/%m/%y"))

def tee(lines, funcs):
    for line in line:
        for func in funcs:
            func.send(line)

def max(key):
    m = -9999999
    val = (yield)
    while val:
        if val > m:
            m = val
        val = (yield)
    return m

def sum(key):
    s = 0
    val = (yield)
    while val:
        s = s + val
        val = (yield)
    return s


if __name__=='__main__':
    data = parse(open('/path/to/csv'))
    tee(data, [max("id"), sum("value")])
