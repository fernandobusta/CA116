#!/usr/bin/env python3

month = int(input())
day = int(input())

day_year = ((month * 30) - 30 + day)

day_of_the_month = (day_year % 7)

if day_of_the_month == 0:
    print(7)
else:
    print(day_of_the_month)
