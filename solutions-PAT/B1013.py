# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/6 0:23
# @File    : B1013.py
# @Software: PyCharm
################################################
# hint
# 数素数：常规的素数判断策略，部分测试点python会超时，
# 在网上看到一种巧妙的判断策略，可以借鉴一下
################################################
import math


def is_prime(n):
    if n <= 1:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(n)) + 2, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def func():
    m, n = map(int, input().split())
    count = 1  # 标记打印的素数个数
    cnt = 0  # 标记素数的个数
    num = 2
    results = []  # 用来存放待输出结果
    while cnt < n:
        if is_prime(num):
            cnt += 1
            if cnt >= m:
                results.append(num)
        num += 1

    for num in results:
        if count == len(results):
            print(num)
        elif count % 10 != 0 and count != len(results):
            print(num, end=" ")
            count += 1
        else:
            print(num)
            count += 1


if __name__ == '__main__':
    func()
