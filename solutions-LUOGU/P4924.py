# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/16 11:23
# @File    : P4924.py
# @Software: PyCharm
################################################
# hint
# 本题本质是一个矩阵旋转的问题
################################################

################################################
# 法一：该方法是常规的方法，不过有几个测试点会超时...
################################################
import copy


def func():
    n, m = map(int, input().split())
    matrix = []  # 初始化方阵
    z = 0  # 方阵元素值
    for i in range(n):  # 填充方阵元素值
        matrix.append([])
        for _ in range(n):
            z += 1
            matrix[i].append(z)

    temp = copy.deepcopy(matrix)  # 创建一个临时数组存储

    for _ in range(m):
        x, y, r, opt = map(int, input().split())
        if opt == 0:  # 第i行第j个变成倒数第i列 第j个 顺时针
            for i in range(x - r - 1, x + r):
                for j in range(y - r - 1, y + r):
                    temp[x - y + j][x + y - i - 2] = matrix[i][j]
            for i in range(x - r - 1, x + r):
                for j in range(y - r - 1, y + r):
                    matrix[i][j] = temp[i][j]
        else:  # 第i行第j个变成第i列 倒数第j个 逆时针
            for i in range(x - r - 1, x + r):
                for j in range(y - r - 1, y + r):
                    temp[x + y - j - 2][y - x + i] = matrix[i][j]
            for i in range(x - r - 1, x + r):
                for j in range(y - r - 1, y + r):
                    matrix[i][j] = temp[i][j]

    # 打印施法后的矩阵
    for row in matrix:
        print(*row, sep=" ")


if __name__ == '__main__':
    func()
