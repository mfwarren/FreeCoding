#!/usr/bin/env python3
# imports go here
from collections import Counter
#
# Free Coding session for 2015-05-17
# Written by Matt Warren
#


def main():
    text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    words = text.split()
    print(len(words))

    d = Counter(words)
    print(d.most_common(5))

if __name__ == '__main__':
    main()
