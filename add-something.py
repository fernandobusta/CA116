#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
    s = int(s)
    a.append(s)
    s = input()

n = int(input())

i = 0
while i < len(a):
        print(a[i] + n)
        i += 1
