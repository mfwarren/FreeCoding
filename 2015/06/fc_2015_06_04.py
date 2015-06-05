#!/usr/bin/env python3
# imports go here
import random

#
# Free Coding session for 2015-06-04
# Written by Matt Warren
#


def linear_regression(x, y):
    length = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    # Σx**2 and Σxy
    sum_x_squared = sum(map(lambda a: a*a, x))
    sum_of_products = sum([x[i] * y[i] for i in range(length)])

    a = (sum_of_products - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x**2) / length))
    b = (sum_y - a * sum_x) / length
    return a, b  # y = ax + b

if __name__ == '__main__':
    simple_data = [[0, 10], [0, 10]]  # slope=1, intercept=0
    print(linear_regression(*simple_data))

    random_data = [list(range(1000)), [random.triangular(20, 99, 70) for i in range(1000)]]  # should be slope ~=0 intercept ~= 70
    print(linear_regression(*random_data))
