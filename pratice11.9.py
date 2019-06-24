#!usr/bin/env python3

from functools import reduce


def average(list):
    return reduce(lambda x, y: x + y, list) / len(list)


test = average(list(range(100)))
print(test)
