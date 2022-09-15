# -*- coding: utf-8  -*-
################################################
# hint
# 这个津津的储蓄计划问题的解决思路就是，用循环枚举每个
# 月的资金流动，逻辑比较简单，但是比较琐碎，需要注意细节
################################################
currMoney = 0
budget = 0
save = 0
flag = 1
month = 0
for i in range(1, 13):
    currMoney += 300
    budget = int(input())
    currMoney -= budget
    if currMoney < 0:
        flag = 0
        month = i
        break
    save += int(currMoney / 100)
    currMoney = currMoney % 100
if flag == 1:
    print(120 * save + currMoney)
else:
    print(-month)
