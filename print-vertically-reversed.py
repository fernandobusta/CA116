#!/usr/bin/env python3

s = input()

m = len(s) - 1
i = 0
while i < len(s):
    print(s[m])
    m = m - 1
    i += 1
