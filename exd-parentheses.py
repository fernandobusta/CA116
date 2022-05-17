#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    current = lines[i]
    j = 0
    while j < len(current) and current[j] != '(':
        j = j + 1
    k = j + 1
    if j < len(current):
        while k < len(current) and current[k] != ')':
            k = k + 1
        print(current[j + 1:k])
    i = i + 1
