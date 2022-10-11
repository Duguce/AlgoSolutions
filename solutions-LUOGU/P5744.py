# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/5 9:26
# @File    : P5744.py
# @Software: PyCharm

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())  # 录入所有学院的信息

for student in students:
    student[1] = int(student[1]) + 1
    student[2] = int(int(student[2]) * 1.2)
    if student[2] > 600:
        student[2] = 600
    print(*student, sep=" ")
