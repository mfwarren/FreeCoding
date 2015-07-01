#!/usr/bin/env python3
# imports go here
import os
import requests

#
# Free Coding session for 2015-06-30
# Written by Matt Warren
#

if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(os.getenv('GITHUB_USERNAME'), os.getenv('GITHUB_PASSWORD')))
    print(r.status_code)
    print(r.json())
