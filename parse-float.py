#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != '.':
    i += 1

print(s[:i])
print(s[i + 1:])
