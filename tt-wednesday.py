#!/usr/bin/env python3

s = input()

while s != 'end':
    tokens = s.split()
    if tokens[0] == '3':
        print(' '.join(tokens))
    s = input()
