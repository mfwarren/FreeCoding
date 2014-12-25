#!/usr/bin/env python3
# imports go here
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
    return filename


def run_todays_file():
    filename = todays_file()
    subprocess.call(['python', filename] + sys.argv[1:])


if __name__ == '__main__':
    run_todays_file()
