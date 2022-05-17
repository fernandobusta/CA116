#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
    a = s.split()
    if int(a[1]) < 10:
        a[2] = str(int(a[2]) + int(a[1]) - 1) + ':50'
        a[1] = str(int(a[1])) + ':00'
    else:
        a[2] = str(int(a[2]) + int(a[1]) - 1) + ':50'
        a[1] = a[1] + ':00'
    print(' '.join(a))
    s = input()
