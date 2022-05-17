#!/usr/bin/env python3

new = ''
new_lines = []
with open('input.txt') as f:
    with open('output.txt', 'w') as g:
        lines = f.readlines()

        i = 0
        while i < len(lines):
            new = ''
            ch = lines[i]
            j = 0
            while j < len(ch):
                if ('A' <= ch[j] and ch[j] <= 'Z'):
                    new = new + '*'
                elif ('a' <= ch[j] and ch[j] <= 'z'):
                    new = new + '*'
                else:
                    new = new + ch[j]
                j += 1
            new_lines.append(new)
            i += 1
        k = 0
        while k < len(new_lines):
            g.write(new_lines[k])
            k += 1
