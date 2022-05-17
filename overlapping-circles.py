#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

a = y1 - y2
b = x1 - x2

min_rad = a * a + b * b
if (min_rad < ((r1 + r2) * (r1 + r2))):
    print('yes')
else:
    print('no')
