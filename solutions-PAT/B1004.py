# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/3 12:54
# @File    : B1004.py
# @Software: PyCharm
################################################
# hint
# 成绩排名
################################################
def func():
    n = int(input())
    lst = []
    for _ in range(n):
        name, id, score = input().split()
        lst.append([name, id, int(score)])
    lst = sorted(lst, key=lambda l: l[2], reverse=True)  # 按照成绩降序排名
    print(lst[0][0], lst[0][1], sep=" ")  # 打印成绩最高学生的学号和姓名
    print(lst[-1][0], lst[-1][1], sep=" ")  # 打印成绩最低学生的学号和姓名


if __name__ == '__main__':
    func()
