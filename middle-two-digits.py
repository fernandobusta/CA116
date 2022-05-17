#!/usr/bin/env python3

n = int(input())

#six digit number, lets say: aabbcc

aa = n // 10000
bb = (n - (aa * 10000)) // 100

print(bb)
