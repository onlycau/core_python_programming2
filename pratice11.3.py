#!/usr/bin/env python3


def max2(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1


def min2(num1, num2):

    if num1 < num2:
        return num1
    else:
        return num2


def max(*args):
    if not args:
        raise ValueError('at least one arg.')
    result = args[0]
    for num in args:
        result = max2(result, num)
    return result


def test():

    my_list = [[1, 3, 5, 7], ['qer', 'werr', 'qrrer'], 'sdfjjaf']
    for i in my_list:
        print(max(i))

if __name__ == "__main__":

    test()
