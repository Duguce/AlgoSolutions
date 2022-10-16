# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/14 8:59
# @File    : P1563.py
# @Software: PyCharm
################################################
# hint
# 本题用模拟的方法就能解决。不过这道题卡了1h左右，很简单
# 的一个点:判断小人朝向及向左向右的时候，分支结构出问
# 题了，我用了两个if，等于一次循环进行了两次判断。引以为戒！
################################################
def func():
    n, m = map(int, input().split())

    person = []  # 用于录入每个玩具小人及其朝向
    for _ in range(n):
        t, p = input().split()
        person.append([int(t), p])

    index = 0

    for _ in range(m):
        t, s = map(int, input().split())
        # if t == 0:
        #     if person[index][0] == 1:
        #         index = (index + s) % n
        #     else:
        #         index = (index + n - s) % n
        # else:
        #     if person[index][0] == 1:
        #         index = (index + n - s) % n
        #     else:
        #         index = (index + s) % n
        if t == person[index][0]:
            index = (index + n - s) % n
        else:
            index = (index + s) % n
    print(person[index][1])


if __name__ == '__main__':
    func()
