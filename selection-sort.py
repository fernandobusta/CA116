#!/usr/bin/env python3

a = []

#create the list
s = input()
while s != 'end':
    s = int(s)
    a.append(s)
    s = input()
#order the list
#tmp = 0
#i = 1
#j = 0
#small = 0
#do this until the list is ordered
#while i < len(a):
#find the smallest value
#    if a[i] < a[smallest]:
#        smallest = i #position of the smallest no.
#swap this no. on the first unordered pos.
#        tmp = a[j]
#        a[j] = a[smallest]
#        j += 1
#    i += 1
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    i += 1

i = 0
while i < len(a):
    print(a[i])
    i += 1
