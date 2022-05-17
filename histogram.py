#!/usr/bin/env python3

a = []

#build the list first
s = input()
while s != 'end':
    s = int(s)
    a.append(s)
    s = input()

#times the digit is repeated
replay = 0
#the actual digit
i = 0
while i < 10:
    #find replay
    j = 0
    while j < len(a):
        if a[j] == i:
            replay += 1
        j += 1
    print(i, '*' * replay)
    replay = 0
    i += 1
