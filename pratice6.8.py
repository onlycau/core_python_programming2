#!/usr/bin/env python3

import random

"""translate number in english"""


class number_translate(object):

    def __init__(self, n):

        self.n = n
        self.number0_10 = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10:'ten',}
        self.number11_19 = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        self.number20_90 = {0: '', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6 : 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

    def hundered(self, h):
        h = int(h)
        print('%s hundered ' % self.number0_10[h], end = '')

    def ten(self, t):
        t = int(t)
        print('%s' % (self.number20_90[t]), end = '')

    def unit(self, u):
        u = int(u)
        print('%s' % (self.number0_10[u]))

    def translate(self, n):

        if n / 100 > 0:
            self.hundered(n / 100)
            if int(n / 10 % 10) == 1:
                print('and %s' % self.number11_19[n % 100])
            else:
                self.ten(n / 10 % 10)
                self.unit(n % 10)
        elif n / 10 > 1:
            self.ten(n / 10)
            if n % 10 > 0:
                print('-')
                self.unit(n % 10)
        elif n / 10 == 1:
            print(self.number11_19[n])
        else:
            print(self.number0_10[n])


def test():
    n = random.randint(0, 999)
    number_translate(n).translate(n)


if __name__ == '__main__':
    test()
