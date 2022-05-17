#!/usr/bin/env python3

s = input()

i = 0

#day of the week
while i < len(s) and s[i] != ' ':
    i += 1
day_week = s[:i]

#number
#sumamos 1 para que elimine el ' ' de delante
i += 1
j = i
while j < len(s) and s[j] != ' ':
    j += 1
day = s[i:j]

#month
j += 1
k = j
while k < len(s) and s[k] != ' ':
    k += 1
month = s[j:k - 1]

#year
k += 1
year = k
while year < len(s) and s[year] != ' ':
    year += 1
year = s[k:year]

#output: date changed
print(month, day + ',', year, '(' + day_week + ')')
