#!/usr/bin/env python3

n = int(input())

if (n == 1):
    print('not prime')
elif (((n % 2 != 0) and (n % 3 != 0)) or ((n == 2) or (n == 3))):
    print('prime')
else:
    print('not prime')
