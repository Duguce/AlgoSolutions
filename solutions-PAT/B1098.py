# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/21 13:59
# @File    : B1098.py
# @Software: PyCharm
################################################
# hint
# 岩洞施工
################################################
def func():
    n = int(input())
    h_lst = list(map(int, input().split()))
    l_lst = list(map(int, input().split()))
    gap = min(h_lst) - max(l_lst)
    if gap >= 1:
        print("Yes", gap, sep=" ")
    else:
        print("No", 1 - gap, sep=" ")


if __name__ == '__main__':
    func()
