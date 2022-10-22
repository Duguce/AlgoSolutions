# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/22 8:59
# @File    : P1591.py
# @Software: PyCharm
################################################
# hint
# 阶乘数码
################################################
def factorial(n, lst):
    """阶乘运算"""
    lst.extend([0] * (n - len(lst) + 1))
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] * i
    return lst


def func():
    t = int(input())
    lst = [0, 1]  # 用于存储1-n!中的每一个数码
    for _ in range(t):
        n, a = map(int, input().split())
        if n > len(lst) - 1:
            lst = factorial(n, lst)
        print(str(lst[n]).count(str(a)))


if __name__ == '__main__':
    func()
