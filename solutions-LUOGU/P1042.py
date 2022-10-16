# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/14 8:30
# @File    : P1042.py
# @Software: PyCharm
################################################
# hint
# 本题要求在11分制和21分值下，根据每个求的胜负，记录比赛
# 的结果。题不难，正常模拟就好，就是不懂乒乓球的胜负规则，
# 花了点时间去了解了一下。
################################################
s = ""  # 定义一个字符串用于接收比赛信息
while True:
    s += input().strip()
    if "E" in s:
        s = s[:s.find("E") + 1]
        break

w, l = 0, 0  # 记录“W”、"L"在字符串中出现的次数

for i in s:  # 11分制下的比赛
    if i == "W":
        w += 1
    if i == "L":
        l += 1
    if i == "E":
        print(f"{w}:{l}")
    if abs(w - l) >= 2 and (w >= 11 or l >= 11):
        print(f"{w}:{l}")
        w, l = 0, 0  # 一局分出胜负，分数归零
print()
w, l = 0, 0  # 记录“W”、"L"在字符串中出现的次数
for i in s:  # 21分制下的比赛
    if i == "W":
        w += 1
    if i == "L":
        l += 1
    if i == "E":
        print(f"{w}:{l}")
    if abs(w - l) >= 2 and (w >= 21 or l >= 21):
        print(f"{w}:{l}")
        w, l = 0, 0  # 一局分出胜负，分数归零
