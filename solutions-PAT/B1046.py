# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/28 8:39
# @File    : B1046.py
# @Software: PyCharm
################################################
# hint
# 划拳
################################################
def func():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    count_a = 0  # 记录甲需要喝的杯数
    count_b = 0  # 记录乙需要喝的杯数
    for l in lst:
        if l[0] + l[2] == l[1] and l[0] + l[2] != l[3]:  # 如果甲赢
            count_b += 1
        elif l[0] + l[2] != l[1] and l[0] + l[2] == l[3]:  # 如果乙赢
            count_a += 1
    print(count_a, count_b, sep=" ")


if __name__ == '__main__':
    func()
