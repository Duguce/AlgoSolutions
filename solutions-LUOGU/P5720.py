# -*- coding: utf-8  -*-
a = int(input())
day = 1
while a // 2 != 1 and a != 1:
    a -= a // 2
    day += 1
print(day)