# -*- coding: utf-8  -*-
import math

m, t, s = map(int, input().split())
if t == 0:
    sy = 0
else:
    if s % t == 0:
        sy = max(m - s / t, 0)
    else:
        sy = max(m - math.ceil(s / t), 0)
print(int(sy))
