# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/19 20:55
# @File    : P1320.py
# @Software: PyCharm
################################################
# hint
# 本题是相当于把【P1319.py】反过来
################################################
arr = input().strip()
n = len(arr)
for i in range(n - 1):
    arr += input().strip()

arr0 = list(map(len, [i for i in arr.split("1") if i != ""]))
arr1 = list(map(len, [i for i in arr.split("0") if i != ""]))
if arr[0] == "1":
    arr0 = [0] + arr0

arr2 = [0] * (len(arr0) + len(arr1))
for i in range(0, len(arr0)):
    arr2[i * 2] = arr0[i]
for i in range(0, len(arr1)):
    arr2[i * 2 + 1] = arr1[i]
print(str(n), " ".join(map(str, arr2)))
