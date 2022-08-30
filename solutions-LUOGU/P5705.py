# -*- coding: utf-8  -*-
a = str(input())
b = ''
for s in a[::-1]:
    b = b + s
print(float(b))
