# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/1 20:24
# @File    : B1093.py
# @Software: PyCharm
################################################
# hint
# 字符串A+B
################################################
def func():
    a = input()
    b = input()
    ans = set()
    for c in a:
        if c not in ans:
            ans.add(c)
            print(c, end="")
    for c in b:
        if c not in ans:
            ans.add(c)
            print(c, end="")


if __name__ == '__main__':
    func()
