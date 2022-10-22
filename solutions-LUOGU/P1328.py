# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/17 8:18
# @File    : P1328.py
# @Software: PyCharm
################################################
# hint
# 模拟问题
################################################
def func():
    n, a, b = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    vs_arr = [[0, -1, 1, 1, -1], [1, 0, -1, 1, -1], [-1, 1, 0, -1, 1], [-1, -1, 1, 0, 1], [1, 1, -1, -1, 0]]  # 记录得分规则
    a_score = 0
    b_score = 0
    for i in range(n):
        a_index = i % a
        b_index = i % b
        if vs_arr[a_arr[a_index]][b_arr[b_index]] == 1:
            a_score += 1
        elif vs_arr[a_arr[a_index]][b_arr[b_index]] == -1:
            b_score += 1

    print(a_score, b_score, sep=" ")


if __name__ == '__main__':
    func()
