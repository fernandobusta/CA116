#!/usr/bin/env python3

n = int(input())

dd = (n // 10000) * 100
mm = ((n // 100) - dd) * 10000
yy = n - (dd * 100) - (mm // 100)

print(mm + dd + yy)
