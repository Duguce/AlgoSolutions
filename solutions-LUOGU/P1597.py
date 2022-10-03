# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/29 21:13
# @File    : P1597.py
# @Software: PyCharm

s = input()  # 接收字符串
dic = {"a": "0", "b": "0", "c": "0"}  # 定义初始值
for index in range(len(s)):  # 遍历每一个字符
    if s[index] == ";":  # 以";"分割每一个公式
        dic[s[index - 4]] = eval(s[index - 1]) if "0" <= s[index - 1] <= "9" else dic[str(s[index - 1])]

print(dic['a'], dic['b'], dic['c'])
