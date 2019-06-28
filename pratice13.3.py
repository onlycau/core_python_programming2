#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Money_fmt(object):

    def __init__(self, count):
        self.count = count

    def __nonzero__(self):
        if self.count != 0:
            return True

    def __str__(self):
        return self.yuan()

    def __repr__(self):
        return str(float(self.count))

    def update(self, new_count):
        self.count = new_count
        print('count is %f now.' % new_count)

    def yuan(self):
        symbol = '￥'
        amount = str(abs(self.count)).split('.')
        if self.count < 0:
            symbol = '-' + symbol
        amount_integer = amount[0]
        if len(amount) > 1:
            amount_decimal = amount[1]
            spot = '.'
        else:
            amount_decimal = ''
            spot = ''
        reversal = amount_integer[::-1]
        reversa_splits = [reversal[i:i + 3] for i in range(0, len(reversal), 3)]
        amount_integer = ','.join(reversa_splits)[::-1]
        return symbol + amount_integer + spot + amount_decimal


def test():
    money = Money_fmt(-324234.465555)
    print(money)


if __name__ == '__main__':

    test()
