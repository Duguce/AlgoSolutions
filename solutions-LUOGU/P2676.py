# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/30 8:48
# @File    : P2676.py
# @Software: PyCharm
################################################
# hint
# Bookshelf B:排序
################################################
def func():
    n, b = map(int, input().split())
    lst = [int(input()) for _ in range(n)]
    lst = sorted(lst, reverse=True)
    sum_n = 0
    count = 0
    for i in range(n):
        if sum_n >= b:
            print(count)
            return
        else:
            sum_n += lst[i]
            count += 1


if __name__ == '__main__':
    func()
