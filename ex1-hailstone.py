#!/usr/bin/env python3

a = int(input())
b = int(input())

next = 0

if (a % 2 == 0):
    next = a // 2
    if b == next:
        print('yes')
    else:
        print('no')
else:
    next = 3 * a + 1
    if b == next:
        print('yes')
    else:
        print('no')
