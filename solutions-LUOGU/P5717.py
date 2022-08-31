# -*- coding: utf-8  -*-

a = list(map(int, input().split(' ')))
a.sort()
if a[0] + a[1] > a[2]:
    if a[0] * a[0] + a[1] * a[1] == a[2] * a[2]:
        print('Right triangle')
    elif a[0] * a[0] + a[1] * a[1] > a[2] * a[2]:
        print('Acute triangle')
    else:
        print('Obtuse triangle')
    if a[0] == a[1] or a[1] == a[2]:
        print('Isosceles triangle')
    if a[0] == a[1] == a[2]:
        print('Equilateral triangle')
else:
    print('Not triangle')
