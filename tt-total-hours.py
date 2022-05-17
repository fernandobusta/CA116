#!/usr/bin/env python3

a = []
total = 0

s = input()
while s != 'end':
    a = s.split()
    time = int(a[2])
    total += time
    s = input()

print(total)
