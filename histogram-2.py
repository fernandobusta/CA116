#!/usr/bin/env python3

n = int(input())

a = []

i = 0
while i < n:
    s = int(input())
    a.append(s)
    i += 1

i = 0
while i < len(a):
    print(a[i] * '*')
    i += 1
