#!/usr/bin/env python3
# imports go here
import math

#
# Free Coding session for 2015-03-22
# Written by Matt Warren
#


def glasses_prescription(far_point):
    # far point is measured in cm
    diopters = 100.0 / far_point

    # round to nearest .25
    diopters = math.ceil(diopters * 100 / 25) * 25 / 100
    return diopters

if __name__ == '__main__':
    print(glasses_prescription(24))
