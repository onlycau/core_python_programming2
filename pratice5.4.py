#!/usr/bin/env python3


"""this is a pratice program to judge one year"""


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def test():

    years = [1542, 4252, 333, 4000, 800, 600, 3965]
    result = list(filter(leap_year, years))
    print(result)


if __name__ == '__main__':
    test()
