# -*- coding: utf-8  -*-
import math

h, r = map(int, input().split())  # 输入小圆桶的深度h和底面半径r
v = math.pi * r * r * h  # 求出桶的体积
count = math.ceil(20 * 1000 / v)  # 求出大象需要喝水的桶数
print(count)
