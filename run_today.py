#!/usr/bin/env python3
# imports go here
import os
import sys
import subprocess
import datetime

#
# Free Coding session for 2014-11-22
# Written by Matt Warren
#


def todays_file():
    today = datetime.date.today()
    filename = today.strftime("%Y/%m/fc_%Y_%m_%d.py")
    if os.path.isfile(filename):
        return filename
    filename = today.strftime('%Y/%m/fc_%d/__init__.py')
    if os.path.isfile(filename):
        return filename
    filename = today.strftime("%Y/%m/fc_%Y_%m_%d.swift")
    if os.path.isfile(filename):
        return filename
    return None


def run_todays_file():
    filename = todays_file()
    if filename is not None and filename.endswith('.py'):
        subprocess.call(['python3', filename] + sys.argv[1:])
    elif filename is not None and filename.endswith('.swift'):
        subprocess.call(['swift', filename] + sys.argv[1:])
    else:
        print("No file to run")


if __name__ == '__main__':
    run_todays_file()
