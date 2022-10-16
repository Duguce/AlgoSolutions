# -*- coding: utf-8  -*-
# @Author  : Duguce
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/15 10:01
# @File    : P1303.py
# @Software: PyCharm
################################################
# 本题一个高精度乘法问题
################################################

################################################
# 法一：这个方法最后一个测试点超时了，过不了...
################################################
# def func():
#     a = input().strip()
#     b = input().strip()
#     if a == "0" or b == "0":
#         return print(0)
#     ans = ""  # 用于存储a*b的值
#     carry = 0  # 进位标志
#     for i in range(len(b) - 1, -1, -1):
#         temp = ""  # 用于暂存b的每一位和a的乘积
#         for j in range(len(a) - 1, -1, -1):
#             carry, mod = divmod(int(a[j]) * int(b[i]) + carry, 10)
#             temp = str(mod) + temp
#         ans = add(ans, temp + "0" * (len(b) - 1 - i))
#     print(ans)
#
#
# def add(a, b):
#     if len(a) < len(b):
#         a, b = b, a
#     b = "0" * (len(a) - len(b)) + b  # 对位数较小的值进行补位
#
#     carry = 0  # carry进位标志
#     c = ""  # 存储得到的加数
#     for i in range(len(a) - 1, -1, -1):  # 从个位数开始遍历
#         carry, mod = divmod(int(a[i]) + int(b[i]) + carry, 10)
#         c = str(mod) + c
#
#     return str(carry) + c if carry != 0 else c


################################################
# 法二：利用python的特性硬上...
################################################
def func():
    a = int(input())
    b = int(input())
    ans = a * b

    print(ans)


if __name__ == '__main__':
    func()
