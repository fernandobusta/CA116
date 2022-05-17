#!/usr/bin/env python3

n = int(input())

#six digit number: aabbcc

aa = n // 10000

bb = (n - (aa * 10000)) // 100
b_second = (bb // 10)
b_first = (bb - (b_second * 10)) * 10
bb_swapped = b_first + b_second

print(bb_swapped)
