#!/usr/bin/env python3

s = input()

value = 0
i = 0
while i < len(s):
    m = int(s[i])
    value = value + m
    i += 1
print(value)
