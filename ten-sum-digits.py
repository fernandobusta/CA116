#!/usr/bin/env python3

temp = 0
number_of_zeros = 11
m = 10
i = 0
while i < m:
    n = int(input())
    if n >= 0:

        while number_of_zeros >= 10:
            sth = n // 10
            sth = sth * 10
            number_of_zeros = n - sth

        temp = number_of_zeros + temp

    else:
        n = n * (-1)
        while number_of_zeros >= 10:
            sth = n // 10
            sth = sth * 10
            number_of_zeros = n - sth

        temp = number_of_zeros + temp

    number_of_zeros = 11
    i = i + 1

print(temp)
