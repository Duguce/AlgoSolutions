# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/27 18:27
# @File    : P1093.py
# @Software: PyCharm
################################################
# hint
# 奖学金：排序问题
################################################
def func():
    n = int(input())
    lst = []
    for i in range(n):
        chinese, math, english = map(int, input().split())
        lst.append([i + 1, sum([chinese, math, english]), chinese])

    lst = sorted(lst, key=lambda l: (l[1], l[2], -l[0]), reverse=True)  # 排序

    for l in lst[:5]:  # 打印前五名
        print(*(l[:2]), sep=" ")


if __name__ == '__main__':
    func()
