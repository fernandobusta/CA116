#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["dog", "cat", "mouse"]

# And the rest of your fragment goes here.
#
#

i = 0
while i < len(a) and len(a[i]) < 6:
    i += 1

if i < len(a):
    print(a[i])
