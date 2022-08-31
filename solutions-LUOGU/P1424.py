# -*- coding: utf-8  -*-
x, n = map(int, input().split(' '))
s = 0
for i in range(1, n + 1):
    if x <= 5:
        s = s + 250
    x = x + 1
    if x == 8:
        x = 1
print(s)
