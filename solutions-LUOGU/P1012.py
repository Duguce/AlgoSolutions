# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/31 8:43
# @File    : P1012.py
# @Software: PyCharm
################################################
# hint
# 拼数
################################################
def func():
    n = int(input())
    lst = input().split()

    for i in range(n):
        for j in range(i, n):
            if lst[i] + lst[j] < lst[j] + lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

    print(*lst, sep="")


if __name__ == '__main__':
    func()
