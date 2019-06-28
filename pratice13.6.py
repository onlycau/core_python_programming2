#!/usr/bin/env python3
# -*-coding:utf-8 -*-


import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)


class Line(object):

    def __init__(self, x=Point(), y=Point()):
        self.x = x
        self.y = y
        self.length = self.length()
        self.slope = self.slope()

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

    def length(self):
        return math.sqrt((self.x.x - self.y.x)**2 + (self.x.y - self.y.y)**2)

    def slope(self):
        if self.x.y == self.y.y:
            return 0
        else:
            return (self.y.y - self.x.y) / (self.y.x - self.x.x)


if __name__ == '__main__':
    point1 = Point(2, 3)
    point2 = Point(3, 5)
    line = Line(point1, point2)
    print(line, line.length, line.slope)
