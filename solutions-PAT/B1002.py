# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/2 11:12
# @File    : B1002.py
# @Software: PyCharm
################################################
# hint
# 写出这个数：计算一个数的各位数之和，并用汉语拼音表示
################################################
def func():
    n = input()
    lst = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']  # 记录拼音数字
    sum_n = str(sum(int(i) for i in n))  # 计算数字的各位数之和
    ans = [lst[int(j)] for j in sum_n]  # 将各位数字之和用汉语拼音表示
    print(*ans, sep=" ")


if __name__ == '__main__':
    func()
