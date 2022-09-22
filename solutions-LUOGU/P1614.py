# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/16 12:09
# @File    : P1614.py
# @Software: PyCharm
################################################
# hint
# 本题不多说，不过要注意给初始解一个尽量大的值
################################################
n, m = map(int, input().split())
arr = []
ans = 1000000
for _ in range(n):
    arr.append(int(input()))

for i in range(n - m + 1):
    curr = 0
    for j in range(i, i + m):
        curr += arr[j]
    if curr < ans:
        ans = curr
print(ans)
