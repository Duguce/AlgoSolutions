# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/18 8:21
# @File    : P5732.py
# @Software: PyCharm
################################################
# hint
# 杨辉三角的递推公式如下
# f[i][j] = f[i-1][j-1] + f[i-1][j]
################################################
n = int(input())  # 定义输出杨辉三角的行数
f = [[0 for _ in range(i + 1)] for i in range(n)]
f[0][0] = 1
for i in range(0, n):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            f[i][j] = 1
        else:
            f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
for arr in f:
    print(*arr, sep=' ')
