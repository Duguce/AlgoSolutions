# -*- coding: utf-8  -*-
################################################
# hint
# 本题是一个求极差的问题，大致思路就是通过循环获取最大
# 值和最小值，然后用两者相减即可求出极差
################################################
n = int(input())
a = list(map(int, input().split(' ')))
max = 0
min = 1000
for i in a:
    if max < i:
        max = i
    if min > i:
        min = i
range = max - min
print(range)
