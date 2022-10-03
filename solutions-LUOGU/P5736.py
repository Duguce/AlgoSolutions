# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/2 14:30
# @File    : P5736.py
# @Software: PyCharm
################################################
# hint
# 本题的核心还是判断质数，但需要注意的是，本题要求去除数
# 组中不是质数的数字，如果直接用pop()函数的话，那么在数
# 组中通过一次遍历操作很容易出错，所以可以再定义一个新的
# 数组用于存储原数组是质数的数字，再打印输出就可以了
################################################
import math


def isPrime(n):
    """判断是否为质数"""
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


n = int(input())
arr = [int(a) for a in input().split()]
ans = []

for i in range(0, n):
    if isPrime(arr[i]):
        ans.append(arr[i])

print(*ans, sep=" ")
