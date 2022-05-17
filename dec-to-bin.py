#!/usr/bin/env python3

n = int(input())
bin = ''
rem = 0

i = 0
while (2 ** i) < n:
    min = 2 ** i
    i += 1

exp = i - 1
rem = n
while exp >= 0:
    bin = bin + str(rem // (2 ** exp))
    rem = n
    rem = n % (2 ** exp)
    exp -= 1

print(bin)
