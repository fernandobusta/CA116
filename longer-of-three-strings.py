#!/usr/bin/env python3

first = input()
second = input()
third = input()

if (len(second) < len(first)) and (len(third) < len(first)):
    print(first)
elif (len(first) < len(second)) and (len(third) < len(second)):
    print(second)
else:
    print(third)
