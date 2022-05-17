#!/usr/bin/env python3

s = input()
even = []
odd = []

while s != 'end':
    s = int(s)
    if s % 2 == 0:
        even.append(s)
    else:
        odd.append(s)
    s = input()

i = 0
while i < len(even):
    print(even[i])
    i += 1

i = 0
while i < len(odd):
    print(odd[i])
    i += 1
