# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/23 9:36
# @File    : P1271.py
# @Software: PyCharm
################################################
# hint
# 排序
################################################
def func():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(*sorted(lst), sep=" ")


if __name__ == '__main__':
    func()
