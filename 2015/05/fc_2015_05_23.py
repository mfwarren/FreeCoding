#!/usr/bin/env python3
# imports go here
import math
#
# Free Coding session for 2015-05-23
# Written by Matt Warren
#


def main():
    print("HI")

    tot = 0
    for i in range(0, 20, 5):
        print(i)
        tot += math.sqrt(i)

    print(tot)


if __name__ == '__main__':
    main()
