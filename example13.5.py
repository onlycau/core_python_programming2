#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Any_iter(object):

    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self, howmany=1):
        retval = []
        for each_item in range(howmany):
            try:
                retval.append(next(self.iter))
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


def test():

    a = Any_iter(range(10), True)
    i = iter(a)
    for j in range(1, 5):
        'i.next(j) no longer work with python3'
        print(j, ':', next(i), i.__next__(j))


if __name__ == '__main__':

    test()