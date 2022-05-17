#!/usr/bin/env python3

a = []

i = 0
s = input()
while s != 'end':
    a.append(s)
    s = input()
    i += 1

i = 0
while i < len(a):
    print(i, len(a), a[i])
    i += 1
