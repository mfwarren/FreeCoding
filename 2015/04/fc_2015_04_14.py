#!/usr/bin/env python3
# imports go here
import subprocess
import os

#
# Free Coding session for 2015-04-14
# Written by Matt Warren
#


def check_ruby_version():
    return subprocess.check_output(['ruby', '--version'])


def rbenv_version():
    if os.path.exists('.ruby_version'):
        with open('.ruby_version', 'r') as f:
            v = f.read()
            return v
    return None

if __name__ == '__main__':
    print(check_ruby_version())
    print(rbenv_version())
