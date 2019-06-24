#!/usr/bin/env python3


num_str = input("enter a number:")
num_num = int(num_str)
fac_list = list(range(1, num_num + 1))
print('before:', fac_list)

i = 0
copy = fac_list[:]
while i < len(copy):

    if num_num % copy[i] == 0:
        fac_list.remove(copy[i])
    i = i + 1


print('after:', fac_list)
