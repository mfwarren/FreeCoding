#!/usr/bin/env python
#imports go here
import os
import fnmatch

#
# Free Coding session for 2014-10-05
# Written by Matt Warren
#

def find_files(root, pattern):
    for path, directories, filenames in os.walk(root):
        for name in fnmatch.filter(filenames, pattern):
            yield os.path.join(path, name)

if __name__=='__main__':
    for f in find_files('.', '*.py'):
        with open(f) as file:
            print f, sum([len(x) for x in file.readlines()])
