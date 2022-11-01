# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/29 9:29
# @File    : P1152.py
# @Software: PyCharm
################################################
# hint
# 欢乐的跳，模拟方法即可解决
################################################
def func():
    lst = list(map(int, input().split()))
    diff = []
    for i in range(len(lst) - 1):
        if abs(lst[i] - lst[i + 1]) not in diff:
            diff.append(abs(lst[i] - lst[i + 1]))
    for j in range(1, len(lst) - 1):
        if j not in diff:
            print("Not jolly")
            return
    print("Jolly")


if __name__ == '__main__':
    func()
