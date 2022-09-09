# -*- coding: utf-8  -*-
################################################
# hint
# 本例是求解序列中最长连号的长度，大致思路为设置两个初始
# 变量（最大连号个数和当前连号个数），循环遍历序列的元素
# 值，当当前元素比下一个元素小1时，当前连号个数加1，否则
# 比较一下最大连号个数和当前连号个数的大小，若小于，则将
# 当前连号个数赋给最大连号个数，并将当前连号个数清为1
# 易错点：特别需要注意的是连号连到末尾的情况，这种情况下，
# 如果使用if...else...的结构则无法将currlong值赋给maxlong
# 在这里我采用了三个if的语句结构，确保每一次循环都可以判断
# 一下currlong是否比maxlong大
################################################
n = int(input())
a = list(map(int, input().split(' ')))
maxLong = 1
currLong = 1
for i in range(0, len(a) - 1):
    if a[i] + 1 == a[i + 1]:
        currLong += 1
    if maxLong < currLong:
        maxLong = currLong
    if a[i] + 1 != a[i + 1]:
        currLong = 1
print(maxLong)
