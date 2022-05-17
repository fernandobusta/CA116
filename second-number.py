#!/usr/bin/env python3

s = input()

#i and j: variables of the two first iterations
i = 0
while i < len(s) and (s[i] < '0' or '9' < s[i]):
    i += 1

j = i + 1
if i < len(s):
    while j < len(s) and ('0' < s[j] and s[j] < '9'):
        j += 1

#j and k: variables of the last two iterations
while j < len(s) and (s[j] < '0' or '9' < s[j]):
    j += 1

if j < len(s):
    k = j + 1
    while k < len(s) and ('0' < s[k] and s[k] < '9'):
        k += 1
    print(s[j:k], j)
