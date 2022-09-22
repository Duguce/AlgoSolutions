# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/22 10:23
# @File    : P1765.py
# @Software: PyCharm
sentence = input()  # 读入原始句子
ans = 0
one = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w']  # 将只需要按一次的字母记录在one列表中
two = ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x']  # 将需要按两次的字母记录在two列表中
three = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']  # 将需要按三次的字母记录在three列表中
four = ['s', 'z']  # 将需要按四次的字母记录在four列表中
for i in range(len(sentence)):
    if sentence[i] in one:
        ans += 1
    elif sentence[i] in two:
        ans += 2
    elif sentence[i] in three:
        ans += 3
    elif sentence[i] in four:
        ans += 4
    if sentence[i] == ' ':
        ans += 1
print(ans)
