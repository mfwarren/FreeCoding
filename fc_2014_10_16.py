#!/usr/bin/env python
#imports go here
import os

#
# Free Coding session for 2014-10-16
# Written by Matt Warren
#

def get_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            yield filename

def count_lines(file):
    n = 0
    with open(file) as f:
        while f.readline():
            n += 1
    return n

def print_file_line_count(f):
    print "%-26s %5s" % (f, count_lines(f))

if __name__=='__main__':
    [print_file_line_count(f) for f in get_files('.')]
