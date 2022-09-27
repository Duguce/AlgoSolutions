# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/23 10:04
# @File    : P1200.py
# @Software: PyCharm

groupName = input()
starName = input()
a = 1
b = 1
for i in groupName:  # 取出小组中的每一个字符
    a = a * (ord(i) - ord('A') + 1)
for j in starName:  # 取出彗星中的每一个字符
    b = b * (ord(j) - ord('A') + 1)

if a % 47 == b % 47:
    print('GO')
else:
    print('STAY')
