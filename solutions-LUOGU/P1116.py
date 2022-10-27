# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/24 21:51
# @File    : P1116.py
# @Software: PyCharm
################################################
# hint
# 车厢倒置，本题本质是一个冒泡排序题
################################################
def func():
    n = int(input())
    lst = []
    while len(lst) < n:
        lst.extend(list(map(int, input().split())))
    count = 0
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                flag = True
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                count += 1
        if not flag:
            break
    print(count)


if __name__ == '__main__':
    func()
