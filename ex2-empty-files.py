#!/usr/bin/env python3

import sys

a = sys.argv[1:]

i = 0
while i < len(a):
    with open(a[i]) as f:
        ch = f.readlines()
        if len(ch) <= 0:
            print(a[i])
    i += 1
