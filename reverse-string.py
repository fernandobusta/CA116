#!/usr/bin/env python3

s = input()

t = ""
letter = len(s) - 1
i = 0
while i < len(s):
    t = t + s[letter]
    letter = letter - 1
    i += 1
print(t)
