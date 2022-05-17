#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

i = 0
while i < len(a):
    a[i] = int(a[i])
    i += 1

chs = int(a[0])
asterix = a[1:]
solution = ''

i = 0
j = 0
while i < chs:
    k = 0
    while j < chs and j != asterix[k]:
        k += 1
        j += 1
    if k < len(asterix):
        solution = solution + '*'
    else:
        solution = solution + ' '
    i += 1

print('|' + solution + '|')
