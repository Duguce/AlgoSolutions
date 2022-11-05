# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/2 13:57
# @File    : P1104.py
# @Software: PyCharm
################################################
# hint
# 生日：按照年龄大小排序（注意，年龄相同时，输入靠后的先
# 输出）
################################################
def func():
    n = int(input())
    lst = []
    for i in range(n):
        name, year, month, date = input().split()
        lst.append([i + 1, name, int(year), int(month), int(date)])
    lst = sorted(lst, key=lambda l: (l[2], l[3], l[4], -l[0]))
    for l in lst:
        print(l[1])


if __name__ == '__main__':
    func()
