#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
    n = int(s[len(s) - (i + 1)])
    total += n * (2 ** i)
    i += 1

print(total)
