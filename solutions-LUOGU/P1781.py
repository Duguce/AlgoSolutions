# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/3 17:42
# @File    : P1781.py
# @Software: PyCharm
################################################
# hint
# 宇宙总统
################################################
def func():
    n = int(input())
    lst = [[i + 1, int(input())] for i in range(n)]
    lst = sorted(lst, key=lambda l: l[1], reverse=True)
    print(lst[0][0], lst[0][1], sep="\n")


if __name__ == '__main__':
    func()
