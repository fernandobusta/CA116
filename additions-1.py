#!/usr/bin/env python3

left = 0
right = 0
i = 0
while i < 10:
    s = input()
    j = 0
    while j < len(s) and s[j] != '+':
        j += 1
    right = int(s[j + 1:])
    left = int((s[:j]))
    print(left + right)
    i += 1
