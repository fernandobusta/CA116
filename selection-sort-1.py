#!/usr/bin/env python3

a = []

s = input()

while s != 'end':
    s = int(s)
    a.append(s)
    s = input()

i = 0
smaller = i
while i + 1 < len(a):
    if a[smaller] > a[i + 1]:
        smaller = i + 1
    i += 1

print(smaller)
