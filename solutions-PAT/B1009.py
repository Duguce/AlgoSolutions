# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/21 13:38
# @File    : B1009.py
# @Software: PyCharm
################################################
# hint
# 说反话
################################################
def func():
    word_lst = input().split(" ")
    print(*word_lst[::-1], sep=" ")


if __name__ == '__main__':
    func()
