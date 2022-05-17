#!/usr/bin/env python3

n = int(input())

m = 0
print(m)

i = 0
while i < (n - 1):
    if (m < 0):
        m = m * (-1) + 1
        print(m)
    else:
        m = m * (-1) - 1
        print(m)
    i = i + 1
