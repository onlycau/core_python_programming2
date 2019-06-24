#!/usr/bin/env python3

"""create text file ,read and siaplay text file"""

import os
ls = os.linesep


class file_action(object):

    def __init__(self):
        pass

    def makefile(self):
        while True:
            fname = input('please enter the file name:')
            if os.path.exists(fname):
                print('error:%s already exists' % fname)
            else:
                break
        text = []
        print("\nEnter lines('.'y itself to quit.\n")
        while True:
            entry = input('>')
            if entry =='.':
                break
            else:
                text.append(entry)
        #write lines to file with proper line-ending
        fobj = open(fname, 'w')
        fobj.writelines(['%s%s' % (x, ls)for x in text])
        fobj.close()
        print('make file %s done' % fname)

    def readtext(self):
        while True:
            fname = input('enter filename:')
            if not os.path.exists(fname):
                print('Error,%s haven\'t exists')
            else:
                break
        fobj = open(fname, 'r')
        for eachLine in fobj:
            print(eachLine)
        fobj.close()


def test():
    fa = file_action()
    fa.makefile()
    fa.readtext()
    pass


if __name__ == '__main__':
    test()