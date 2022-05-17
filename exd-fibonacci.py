#!/usr/bin/env python3

n = int(input())
a = []

fibo = 1
last = 0
while fibo < n + 1:
    a.append(fibo)
    tmp = fibo
    fibo += last
    last = tmp

j = 0
i = 0
while i < len(a):
    while j < len(a) and a[j] != n:
        j = j + 1
    i = i + 1


if j < len(a) or n == 0:
    print('yes')
else:
    print('no')
