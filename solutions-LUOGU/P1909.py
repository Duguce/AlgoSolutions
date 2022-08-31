# -*- coding: utf-8  -*-
import math

n = int(input())
minCost = 100000001
for _ in range(3):
    x, y = map(int, input().split(' '))
    currCost = math.ceil(n / x) * y
    minCost = min(currCost, minCost)
print(minCost)
