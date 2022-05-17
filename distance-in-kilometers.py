#!/usr/bin/env python3

m = int(input())

km_not_rounded = m // 100

m_not_rounded = m - km_not_rounded * 10

km_rounded = m_not_rounded // 500

km = km_not_rounded + km_rounded

print(km)
