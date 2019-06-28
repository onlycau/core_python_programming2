#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - string repressentation'
        return '%d: %d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        self.hr += other.hr
        self.min += other.min
        return self


def test():

    mon = Time60(11, 11)
    thu = Time60(22, 43)
    print(dir(mon), dir(object))
    print(mon + thu)
    mon += thu
    print(mon)


if __name__ == '__main__':
    test()
