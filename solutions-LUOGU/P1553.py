# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/23 9:25
# @File    : P1553.py
# @Software: PyCharm
################################################
# hint
# 本题的主要思路就是对非整数进行分割，然后对每一部分进行
# 反转，再组合
################################################
s = input()  # 输入一个实数


def reverse(s):
    """反转字符串"""
    return '0' if s == '0' else str(int(s[::-1]))


def reverseNum(s):
    """对非整数实数进行反转"""
    if '.' in s:
        a, b = s.split('.')
        return f'{reverse(a)}.{reverse(reverse(reverse(b)))}'
    if '/' in s:
        a, b = s.split('/')
        return f'{reverse(a)}/{reverse(b)}'
    if '%' in s:
        return f'{reverse(s[:-1])}%'
    return reverse(s)


print(reverseNum(s))
