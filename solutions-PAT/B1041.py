# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/25 9:32
# @File    : B1041.py
# @Software: PyCharm
################################################
# hint
# 考试座位号
################################################
def func():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    to_find = list(map(int, input().split()))
    for t in to_find:
        for l in lst:
            if t == l[1]:
                print(l[0], l[2], sep=" ")
                break


if __name__ == '__main__':
    func()
