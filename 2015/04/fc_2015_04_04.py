#!/usr/bin/env python3
# imports go here
import ast
import os
#
# Free Coding session for 2015-04-04
# Written by Matt Warren
#

basedir = os.path.dirname(__file__)
yesterdays_file = os.path.join(basedir, 'fc_2015_04_03.py')
print("examining yesterdays file", yesterdays_file)
source = ''
with open(yesterdays_file) as f:
    source = f.read()

a = ast.parse(source)
print(a)
print(a.body)
print(a.body[0].names)
print(a.body[0].names[0].name)
print(a.body[0].names[0].asname)
