#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["dog", "cat", "mouse"]

# And the rest of your fragment goes here.
#
#

tmp = a[0]
a[0] = a[len(a) - 1]
a[len(a) - 1] = tmp
