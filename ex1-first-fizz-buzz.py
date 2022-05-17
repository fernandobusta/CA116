#!/usr/bin/env python3

#a number is divisible by 3 and 5 when:
#n % 5 and n % 3 both == 0
n = 1
val = 0
while val != 1:
    n = int(input())
    if n % 3 == 0:
        if n % 5 == 0:
            val = 1
        else:
            val = 0
    elif n % 5 == 0:
        if n % 3 == 0:
            val = 1
        else:
            val = 0
    else:
        val = 0
print(n)
