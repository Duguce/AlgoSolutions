# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/3 21:52
# @File    : P5739.py
# @Software: PyCharm
################################################
# hint
# 本题明确说不使用循环语句，那么我们可以用递归来实现
################################################

def factorial(n):
    """求某数的阶乘"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
print(factorial(n))
