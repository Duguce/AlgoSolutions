# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/10 13:00
# @File    : P5461.py
# @Software: PyCharm
################################################
# hint
# 本题的核心就是进行递归运算
################################################
def pardon(arr, x, y, length):
    """定义赦免规则"""
    if length % 2 == 0:
        length = length // 2
        for i in range(x, x + length):
            for j in range(y, y + length):
                arr[i][j] = 0
        pardon(arr, x + length, y, length)
        pardon(arr, x, y + length, length)
        pardon(arr, x + length, y + length, length)


def func():
    n = int(input())
    arr = [[1 for _ in range(2 ** n)] for _ in range(2 ** n)]  # 定义一个作弊者站成的方阵
    pardon(arr, 0, 0, 2 ** n)
    for row in range(2 ** n):
        print(" ".join(map(str, arr[row])))


if __name__ == '__main__':
    func()
