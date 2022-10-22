# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/21 8:45
# @File    : P1205.py
# @Software: PyCharm
################################################
# hint
# 模拟：方块转换
################################################

def transform1(matrix1, matrix2):
    """顺时针转九十度"""
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[j][n - i - 1]:
                return False
    return True


def transform2(matrix1, matrix2):
    """顺时针转一百八十度"""
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[n - i - 1][n - j - 1]:
                return False
    return True


def transform3(matrix1, matrix2):
    """顺时针二百七十度"""
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[n - j - 1][i]:
                return False
    return True


def transform4(matrix1, matrix2):
    """水平方向镜像反转"""
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[i][n - j - 1]:
                return False
    return True


def transform5(matrix1, matrix2):
    """水平方向镜像反转,后再进行一次1-3的转换"""
    n = len(matrix1)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][n - j - 1] = matrix1[i][j]
    if transform1(temp, matrix2) or transform2(temp, matrix2) or transform3(temp, matrix2):
        return True
    return False


def transform6(matrix1, matrix2):
    """不改变"""
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True


def func():
    n = int(input())
    matrix1 = [list(input().strip()) for _ in range(n)]
    matrix2 = [list(input().strip()) for _ in range(n)]
    if transform1(matrix1, matrix2):
        print(1)
    elif transform2(matrix1, matrix2):
        print(2)
    elif transform3(matrix1, matrix2):
        print(3)
    elif transform4(matrix1, matrix2):
        print(4)
    elif transform5(matrix1, matrix2):
        print(5)
    elif transform6(matrix1, matrix2):
        print(6)
    else:
        print(7)


if __name__ == '__main__':
    func()
