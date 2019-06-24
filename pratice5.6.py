#!/usr/bin/env python3


"""it's a tiny calculator for 2 numbers."""


class calculator(object):

    def __init__(self, num1, num2, action):

        self.name = 'calculator1.0'
        self.num1 = float(num1)
        self.num2 = float(num2)
        self.action = action

    def calculat(self):

        if self.action == "+":
            return self.num1 + self.num2
        if self.action == "-":
            return self.num1 - self.num2
        if self.action == "*":
            return self.num1 * self.num2
        if self.action == "/":
            return self.num1 / self.num2
        if self.action == "%":
            return self.num1 / self.num2
        if self.action == "**":
            return self.num1 ** self.num2


def test():

    num1 = input("num1:")
    action = input("action")
    num2 = input("num2:")
    print(calculator(num1, num2, action).calculat())


if __name__ == "__main__":
    test()
