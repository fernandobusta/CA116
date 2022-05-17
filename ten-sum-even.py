#!/usr/bin/env python3

t = 0
m = 10
i = 0
while i < m:
    n = int(input())
    if (n % 2 == 0):
        t = t + n
    i = i + 1

print(t)
