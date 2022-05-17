#!/usr/bin/env python3

# musical notes: a, b, c, d, e, f, g

s = input()

m = len(s)
i = 0
while i < m:
    if s[i] == 'a' or s[i] == 'b' or s[i] == 'c' or s[i] == 'd':
        print(s[i])
        i = m
    elif s[i] == 'e' or s[i] == 'f' or s[i] == 'g':
        print(s[i])
        i = m
    else:
        i += 1
