#!/usr/bin/env python3

n = int(input())

odd_even = 0
i = 0
while i < n:
    if i < n // 2:
        print(" " * i + "*" + " " * (n - (i * 2) - 2) + "*")
    elif i > n // 2:
        if n % 2 != 0:
            print(" " * (n - 1 - i) + "*" + " " * (odd_even * 2 - n) + "*")
        else:
            print(" " * (n - 1 - i) + "*" + " " * (odd_even * 2 - n - 1) + "*")
    else:
        print(" " * (n // 2) + "*")
    odd_even += 1
    i += 1
