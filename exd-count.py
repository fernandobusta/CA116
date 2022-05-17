#!/usr/bin/env python3

import sys

n = int(sys.argv[1])

i = 0
while (i * i) < n:
    i += 1

j = 0
while j < i:
    print(j)
    j += 1
