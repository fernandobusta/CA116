#!/usr/bin/env python3

acc = 0

#asking for numbers
i = 0
while i < 10:
    n = int(input())
    acc = acc * 10 + n
    i += 1

#printing digits
i = 0
while i < 10:
    print(acc % 10)
    acc = acc // 10
    i += 1
