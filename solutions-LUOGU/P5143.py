# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/1 9:15
# @File    : P5143.py
# @Software: PyCharm
################################################
# hint
# 攀爬者：排序
################################################
import math


def func():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst = sorted(lst, key=lambda l: l[2])  # 对坐标按照高度排序
    dis_sum = 0  # 记录攀爬的总距离
    for i in range(n - 1):
        dis = math.sqrt(
            pow(lst[i + 1][0] - lst[i][0], 2) + pow(lst[i + 1][1] - lst[i][1], 2) + pow(lst[i + 1][2] - lst[i][2], 2))
        dis_sum += dis
    print("%.3f" % dis_sum)


if __name__ == '__main__':
    func()
