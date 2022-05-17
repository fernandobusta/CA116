#!/usr/bin/env python3

s = input()

a = []

while s != 'end':
    a.append(s)
    s = input()

i = 1
while i < len(a) + 1:
    print(a[len(a) - i])
    i += 1
