#!/usr/bin/env python3

n = int(input())
pre = n
curr = 0

m = 5
i = 0
while i < m:
    n = int(input())
    curr = n
    if pre < curr:
        print('higher')
    elif pre == curr:
        print('equal')
    else:
        print('lower')
    pre = n
    i += 1
