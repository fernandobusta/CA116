#!/usr/bin/env python3

t = int(input())
m = 9
i = 0
while i < m:
    n = int(input())
    if (n % 2 == 0):
        if n < t:
            t = n
    i = i + 1

print(t)
