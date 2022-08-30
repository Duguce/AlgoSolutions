# -*- coding: utf-8  -*-
a, b = map(int, input().split(" "))
penPrice = 19
myMoney = a * 10 + b
amount = int(myMoney / penPrice) if myMoney >= penPrice else 0
print(amount)
