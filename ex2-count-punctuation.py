#!/usr/bin/env python3

import sys

n = sys.stdin.readlines()
a = []
a.append(n)

count = 0
i = 0
j = 0
while j < len(a):
    lines = a[i]
    print(a)
    print(lines)
    while i < len(a):
        if lines[i] == '.' or lines[i] == ',':
            count += 1
        elif lines[i] == '!' or lines[i] == '?':
            count += 1
        elif lines[i] == ';' or lines[i] == ':':
            count += 1
        i += 1
    j += 1
print(count)
