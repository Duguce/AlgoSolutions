# -*- coding: utf-8  -*-
################################################
# hint
# 本题我的解决思路本质就是一个模拟的过程，定义一个b数组
# 用于记录每次变化的结果
################################################
n = int(input())
b = [n]
flag = True
while flag:
    if n == 1:
        break
    if n % 2 != 0:
        n = int(n * 3 + 1)
    else:
        n = int(n / 2)
    b.insert(0, n)
    if n == 1:
        flag = False
print(*b, sep=' ')
