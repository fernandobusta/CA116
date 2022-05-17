#!/usr/bin/env python3

sum = 0
m = 5
i = 0
while i < m:
    n = int(input())
    if n < 0:
        n = n * (- 1)
        sum += n
    else:
        sum += n
    i += 1
print(sum)
