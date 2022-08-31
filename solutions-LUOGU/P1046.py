# -*- coding: utf-8  -*-
x = list(map(int, input().split(' ')))
y = int(input()) + 30
num = sum(i <= y for i in x)
print(num)
