#!/usr/bin/env python3

import random

"""random pratice"""


def test():

    M = random.randint(2, 100)
    numbers = []
    numbers_new = []
    for i in range(M):
        numbers.append(random.uniform(0, 2 ** 31 - 1))
    for i in range(M):
        number = random.choice(numbers)
        if number not in numbers_new:
            numbers_new.append(number)
    for i in range(len(numbers_new)):
        for v in range(i, len(numbers_new) - 1):
            if numbers_new[v + 1] < numbers_new[v]:
                numbers_new[v], numbers_new[v + 1] = numbers_new[v + 1], numbers_new[v]
    print(numbers_new)


if __name__ == "__main__":
    test()
