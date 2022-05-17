#!/usr/bin/env python3

a = []

s = input()

while s != 'end':
    a.append(s)
    s = input()

n = int(input())
i = 0
while i < len(a):
    tokens = a[i].split()
    day = int(tokens[0])
    if (day == n):
        print(' '.join(tokens))
    i += 1
