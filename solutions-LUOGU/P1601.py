# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/15 9:44
# @File    : P1601.py
# @Software: PyCharm
################################################
# hint
# 本题是一个高精度加分题。高精度是指在很大的位数情况下进
# 行运算，基本思想是用数组进行模拟加法
################################################
def func():
    a = input().strip()
    b = input().strip()
    if len(a) < len(b):
        a, b = b, a
    b = "0" * (len(a) - len(b)) + b  # 对位数较小的值进行补位

    carry = 0  # carry进位标志
    c = ""  # 存储得到的加数
    for i in range(len(a) - 1, -1, -1):  # 从个位数开始遍历
        carry, mod = divmod(int(a[i]) + int(b[i]) + carry, 10)
        c = str(mod) + c

    if carry != 0:
        print(str(carry) + c)
    else:
        print(c)


if __name__ == '__main__':
    func()
