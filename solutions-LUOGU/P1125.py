# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/20 14:24
# @File    : P1125.py
# @Software: PyCharm
################################################
# hint
# 本题本质是一个词频统计问题(字符级)的变种
################################################
import math


def isPrime(n):
    """质数判别"""
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


arr = [i for i in input().strip()]
dict = {}
for s in arr:
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1
maxn = max(dict.values())
minn = min(dict.values())
if isPrime(maxn - minn):
    print('Lucky Word')
    print(maxn - minn)
else:
    print('No Answer')
    print(0)
