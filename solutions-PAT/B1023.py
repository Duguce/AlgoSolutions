# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/3 20:16
# @File    : B1023.py
# @Software: PyCharm
################################################
# hint
# 组个最小数
################################################
def func():
    lst = list(map(int, input().split()))
    num = []
    for i in range(len(lst)):
        num.extend(i for _ in range(lst[i]))
    num = [n for n in num if n != 0]  # 将不为零的数加入到num数组中
    zeros = [0] * lst[0]  # 记录输入0的个数
    num = [num[0]] + zeros + num[1:]  # 将最小数保存到数组中
    print(*num, sep="")


if __name__ == '__main__':
    func()
