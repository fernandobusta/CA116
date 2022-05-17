#!/usr/bin/env python3

s = input()

a = []
total = 0
oldj = 0

j = 0
i = 0
while i < 4:
    oldj = j
    while j < len(s) and s[j] != '+':
        j += 1
    total += int(s[oldj:j])
    j += 1
    i += 1

last = int(s[j - 1:])
print(total + last)
