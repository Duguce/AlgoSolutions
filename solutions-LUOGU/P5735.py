# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/2 14:05
# @File    : P5735.py
# @Software: PyCharm
import math

pos = []  # 定义一个数组用于存储坐标
for _ in range(3):  # 读取并存储每一行的坐标
    pos.append(input().split())

cir = math.sqrt(
    math.pow(float(pos[0][0]) - float(pos[1][0]), 2) + math.pow(float(pos[0][1]) - float(pos[1][1]), 2)) + math.sqrt(
    math.pow(float(pos[0][0]) - float(pos[2][0]), 2) + math.pow(float(pos[0][1]) - float(pos[2][1]), 2)) + math.sqrt(
    math.pow(float(pos[1][0]) -float(pos[2][0]), 2) + math.pow(float(pos[1][1]) - float(pos[2][1]), 2))

print("%.2f" % cir)
