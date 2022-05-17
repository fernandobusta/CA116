#!/usr/bin/env python3

pos = 0
neg = 0

m = 5
i = 0
while i < m:
    n = int(input())
    if n < 0:
        neg = neg + n
    else:
        pos = pos + n
    i += 1

neg = str(neg)
pos = str(pos)
print(neg, pos)
