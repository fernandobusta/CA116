#!/usr/bin/env python3

i = 0
m = 10
s = ''
while i < m:
    n = input()
    s = s + n
    i += 1

i = 0
while i < 10:
    converted = int(s[i])
    print(converted * '*')
    i += 1
