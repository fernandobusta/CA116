#!/usr/bin/env python3

n = int(input())
c = 1
p = 0
print(p)
print(c)

i = 0
while i < (n - 2):
    print(p + c)
    tmp = p + c
    p = c
    c = tmp
    i = i + 1
