# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/18 8:54
# @File    : P1789.py
# @Software: PyCharm
n, m, k = map(int, input().split())
coordArr = [[0 for _ in range(n)] for _ in range(n)]
while m > 0:
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x - 2, x + 3):
        if i < 0 or i >= n:
            continue
        else:
            coordArr[i][y] = 1
    for i in range(y - 2, y + 3):
        if i < 0 or i >= n:
            continue
        else:
            coordArr[x][i] = 1
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or i >= n or j < 0 or j >= n:
                continue
            else:
                coordArr[i][j] = 1
    m -= 1
while k > 0:
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if i < 0 or i >= n or j < 0 or j >= n:
                continue
            else:
                coordArr[i][j] = 1
    k -= 1

ans = 0
for i in range(n):
    for j in range(n):
        if coordArr[i][j] == 0:
            ans += 1
print(ans)
