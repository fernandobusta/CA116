#!/usr/bin/env python3

m = 10
t = 0
i = 0

while i < m:
    n = int(input())
    if n >= 0:
        t = t + n
    i = i + 1
print(t)
