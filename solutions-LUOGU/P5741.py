# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/13 9:01
# @File    : P5741.py
# @Software: PyCharm
################################################
# hint
# 本题应该是要求用结构体实现，但是python我不知道该怎么
# 用，就用了一个循环遍历的笨办法来实现
################################################
def func():
    n = int(input())
    stu = [input().split() for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(int(stu[i][1]) - int(stu[j][1])) <= 5 and abs(int(stu[i][2]) - int(stu[j][2])) <= 5 and abs(
                    int(stu[i][3]) - int(stu[j][3])) <= 5 and abs(
                int(stu[i][1]) - int(stu[j][1]) + int(stu[i][2]) - int(stu[j][2]) + int(stu[i][3]) - int(
                    stu[j][3])) <= 10:
                print(stu[i][0], stu[j][0], sep=" ")


if __name__ == '__main__':
    func()
