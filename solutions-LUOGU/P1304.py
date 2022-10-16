# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/12 8:30
# @File    : P1304.py
# @Software: PyCharm
################################################
# hint
# 哥德巴赫猜想，该题通过是质数判断和枚举即可解决。需要注
# 意的点在于在对每一个数求两个质数加数，要求第一个加数是
# 尽可能小的质数。因此，我们可以从小到大枚举，在找到第一
# 个结果的时候即跳出循环
################################################
import math


def isPrime(n):
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


def func():
    n = int(input())
    for i in range(4, n + 1, 2):
        if i == 4:
            print('4=2+2')
        else:
            for j in range(2, i):
                if isPrime(j) & isPrime(i - j):
                    print(f"{i}={j}+{i - j}")
                    break


if __name__ == '__main__':
    func()
