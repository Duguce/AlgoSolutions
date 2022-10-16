# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/16 11:01
# @File    : P1009.py
# @Software: PyCharm
################################################
# 阶乘之和
################################################
def func():
    n = int(input())
    ans = 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        ans += factorial
    print(ans)


if __name__ == '__main__':
    func()
