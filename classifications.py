#!/usr/bin/env python3

mark = int(input())

first = 70 <= mark
second = 50 <= mark <= 69
third = 40 <= mark <= 49
fail = mark < 40

print('first:', first)
print('second:', second)
print('third:', third)
print('fail:', fail)
