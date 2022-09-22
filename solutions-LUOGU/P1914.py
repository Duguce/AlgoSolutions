# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/20 14:11
# @File    : P1914.py
# @Software: PyCharm
n = int(input())  # 字母向后移动的位数n
st = input()  # 定义一个变量用于接受输入的字符串

for s in st:
    s = chr(ord(s) + n)
    if ord(s) > ord('z'):
        s = chr(ord(s) - 26)
    print(s, end='')
