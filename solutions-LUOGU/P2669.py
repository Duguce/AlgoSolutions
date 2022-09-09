# -*- coding: utf-8  -*-
k = int(input())
currMoney = 1
totalMoney = 0
day = 1
for _ in range(1, k + 1):
    totalMoney += currMoney
    day -= 1
    if day == 0:
        currMoney += 1
        day = currMoney
print(totalMoney)