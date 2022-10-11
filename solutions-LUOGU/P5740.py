# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/11 9:31
# @File    : P5740.py
# @Software: PyCharm
################################################
# hint
# 本题感觉还是一个比大小的问题...
################################################
def func():
    n = int(input())
    maxScore = 0
    maxIndex = 0
    students = [input().split() for _ in range(n)]
    for s in students:
        if int(s[1]) + int(s[2]) + int(s[3]) > maxScore:
            maxScore = int(s[1]) + int(s[2]) + int(s[3])
            maxIndex = students.index(s)
    print(*students[maxIndex], sep=" ")


if __name__ == '__main__':
    func()
