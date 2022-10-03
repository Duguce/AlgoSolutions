# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/3 9:42
# @File    : P5738.py
# @Software: PyCharm
################################################
# hint
# 本题是一个求平均值的问题，这里我直接用了python3的内置
# 求和函数，当然也可以自己写一个求最大值最小值的函数进行
# 求解
################################################
n, m = map(int, input().split())
scores = []  # 用于记录每名同学的平均分
for _ in range(n):
    arr = [int(i) for i in input().split()]
    arr.remove(max(arr))  # 删除最大值
    arr.remove(min(arr))  # 删除最小值
    score = sum(arr) / len(arr)  # 去当前学生的平均分
    scores.append(score)  # 记录到平均分列表中

print("%.2f" % max(scores))
