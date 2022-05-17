#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
    i = 0
    while i < len(a) and a[i] != s:
        i += 1
    if i >= len(a):
        a.append(s)
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i += 1
