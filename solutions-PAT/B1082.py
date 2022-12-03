# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/29 8:28
# @File    : B1082.py
# @Software: PyCharm
################################################
# hint
# 射击比赛
################################################
import math


def func():
    n = int(input())
    lst = [input().split() for _ in range(n)]
    winner, newbie = "", ""
    winner_score = 10000
    newbie_score = 0
    for i in range(n):
        temp_score = math.sqrt(int(lst[i][1]) ** 2 + int(lst[i][2]) ** 2)
        if temp_score < winner_score:
            winner = lst[i][0]
            winner_score = temp_score
        if temp_score > newbie_score:
            newbie = lst[i][0]
            newbie_score = temp_score
    print(winner, newbie, sep=" ")


if __name__ == '__main__':
    func()
