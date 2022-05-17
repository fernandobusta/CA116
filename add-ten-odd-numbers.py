#!/usr/bin/env python3

i = 0
sum_odd = 0

while i != 10:
    n = int(input())
    confirm = n % 2
    sum_odd = sum_odd + (n * confirm)
    i = i + 1
print(sum_odd)
