# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/4 9:26
# @File    : B1027.py
# @Software: PyCharm
################################################
# hint
# 打印沙漏
################################################
def func():
    n, sign = input().split()
    row = 0
    for i in range(int(n)):  # 以最中间一行为中心，查找需要向上（或向下）扩展的行数
        if (2 * i * (i + 2) + 1) > int(n):
            row = i - 1
            break

    for k in range(row, 0, -1):
        for _ in range(row - k, 0, -1):
            print(" ", end="")
        for _ in range(k * 2 + 1, 0, -1):
            print(sign, end="")
        print()
    for r in range(row + 1):
        for _ in range(row - r, 0, -1):
            print(" ", end="")
        for _ in range(r * 2 + 1, 0, -1):
            print(sign, end="")

        print()

    print(int(n) - (2 * row * (row + 2) + 1))


if __name__ == '__main__':
    func()
