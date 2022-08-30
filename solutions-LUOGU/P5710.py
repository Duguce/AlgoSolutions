# -*- coding: utf-8  -*-
x = int(input())
a, b, c, d = 0, 0, 0, 0
if (x % 2 == 0) and (4 < x <= 12):
    a = 1
if (x % 2 == 0) or (4 < x <= 12):
    b = 1
if (x % 2 == 0) ^ (4 < x <= 12):
    c = 1
if (x % 2 != 0) and (x <= 4 or x > 12):
    d = 1

print(a, b, c, d, sep=' ')
