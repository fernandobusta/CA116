#!/usr/bin/env python3

n = int(input())
pre = n
if n != 0:
    n = int(input())
    curr = n

    while n != 0:
        if pre < curr:
            print('higher')
        elif pre == curr:
            print('equal')
        else:
            print('lower')
        pre = n
        n = int(input())
        curr = n
else:
    pre = 0
