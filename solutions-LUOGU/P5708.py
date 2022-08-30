# -*- coding: utf-8  -*-
import math

a, b, c = map(float, input().split(' '))
p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("%.1f" % area)
