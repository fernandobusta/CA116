#!/usr/bin/env python3

s = input()

#buscar  4 the '.'
i = 0
while i < len(s) and s[i] != '.':
    i += 1

j = i
#only if there is a '.'
if i < len(s):
    #buscar if there is sth after '.'
    while j + 1 < len(s):
        j += 1
    #there are NO digits be4 the '.' NOR after
    if i < 1 and j == i:
        print('0.0')
    #there are NO digits be4 but there ARE after
    elif i < 1 and j > i:
        print('0.' + s[j - 2:])
    #there ARE digits be4 but NOT after
    elif i > 0 and j == i:
        #if that character is a '-' sign
        if s[0] == '-' and i < 2:
            print(s[:i] + '0.0')
        #if it isn't a '-'
        else:
            print(s[:i] + '.0')
    #there ARE digits BOTH be4 and after
    else:
        #if be4 the '.' there is only a '-'
        if s[0] == '-' and i < 2:
            print(s[0] + '0' + s[1:])
        #if there are more characters or not a '-'
        else:
            print(s)

#if there isn't a '.'
else:
    print(s + '.0')
