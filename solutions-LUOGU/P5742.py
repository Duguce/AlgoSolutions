# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/5 10:02
# @File    : P5742.py
# @Software: PyCharm

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())  # 存储每一个学生的信息


def resultJudge(result1, result2):
    """对学生的成就进行评价，判断其是否优秀"""
    if (result1 + result2 > 140) and (result1 * 7 + result2 * 3 >= 800):
        print("Excellent")
    else:
        print("Not excellent")


for student in students:
    resultJudge(int(student[1]), int(student[2]))
