#!/usr/bin/env python3

a = int(input())
b = int(input())
temp = 0

while b != 0:
    n = a // b
    temp = b
    b = a - (b * n)
    a = temp

print(a)
