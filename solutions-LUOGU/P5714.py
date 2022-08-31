# -*- coding: utf-8  -*-
m, n = map(float, input().split(' '))
BIM = m / (n ** 2)
if BIM < 18.5:
    print("Underweight")
elif 18.5 <= BIM < 24:
    print("Normal")
elif BIM >= 24:
    print('%.6g' % BIM)
    print("Overweight")
