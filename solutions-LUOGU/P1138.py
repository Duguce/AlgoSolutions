# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/7 11:21
# @File    : P1138.py
# @Software: PyCharm
################################################
# hint
# 第k小整数
################################################
def func():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = []
    for l in lst:
        if l not in arr:
            arr.append(l)
    arr.sort()
    if k < len(arr):
        print(arr[k - 1])
    else:
        print("NO RESULT")


if __name__ == '__main__':
    func()
