#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
    a = s.split()
    time = int(a[2])
    if time > 1:
        print(s)
    s = input()
