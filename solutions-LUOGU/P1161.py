# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/17 8:03
# @File    : P1161.py
# @Software: PyCharm
################################################
# hint
# 模拟
################################################
n = int(input())  # n次操作
arr = [0] * 2000000
for _ in range(n):
    a, k = map(float, input().split())
    for i in range(1, int(k) + 1):
        if arr[int(i * a)] == 0:
            arr[int(i * a)] = 1
        else:
            arr[int(i * a)] = 0

k = 1
while k <= 2000000:
    if arr[k] == 1:
        print(k)
        break
    k += 1
