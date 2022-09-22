# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/19 21:58
# @File    : P5733.py
# @Software: PyCharm
st = input()  # 输入一个字符串

for s in st:
    if ord('a') <= ord(s) <= ord('z'):
        s = chr(ord(s) + ord('A') - ord('a'))
    print(s, end='')
