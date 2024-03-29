#!/usr/bin/env python3


from time import ctime, sleep


def tsfunc(func):

    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()
    return wrappedFunc


def test():

    @tsfunc
    def foo():
        pass
    foo()
    sleep(4)

    for i in range(2):
        sleep(1)
        foo()


if __name__ == '__main__':
    test()
