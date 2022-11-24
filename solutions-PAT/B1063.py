# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/24 13:39
# @File    : B1063.py
# @Software: PyCharm
################################################
# hint
# 计算谱半径
################################################
import math


def func():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for l in lst:
        temp = math.sqrt(l[0] ** 2 + l[1] ** 2)
        if temp > ans:
            ans = temp
    print("%.2f" % ans)


if __name__ == '__main__':
    func()
