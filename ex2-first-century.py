#!/usr/bin/env python3

import sys

a = []

n = sys.stdin.readlines().strip()

a = n.strip()
print(len(a))
i = 0
while i < len(a) or a[i] >= 100:
    i += 1

if i < len(a):
    print(a[i])
else:
    print(none)
