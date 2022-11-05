# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/5 9:04
# @File    : P1036.py
# @Software: PyCharm
################################################
# hint
# 选数：深度优先搜索
################################################
import math


def is_prime(n):
    """判断质数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def dfs(dfn, sum, pos, n, k, lst):
    """深度优先搜索"""
    if dfn == k:  # 选中的数字个数等于k
        return is_prime(sum)
    ans = 0
    for i in range(pos, n):
        ans += dfs(dfn + 1, sum + lst[i], i + 1, n, k, lst)
    return ans


def func():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(dfs(0, 0, 0, n, k, lst))


if __name__ == '__main__':
    func()
