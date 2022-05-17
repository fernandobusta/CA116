#!/usr/bin/env python3

n = int(input())
c = 1
p = 0

print(p)
print(c)

i = 0
while i < n:
    print(p + c)
    tmp = p + c
    p = c
    c = tmp

    i = p + c
