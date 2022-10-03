# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/28 19:28
# @File    : P1598.py
# @Software: PyCharm
################################################
# hint
# 这道题以上来没有思路，后来看了CSDN上的一篇题解才反应过
# 来。对于这种看似奇怪的打印格式，不要慌，要明白打印始终
# 都是从上到下，从左到右打印的。明白这一点后，问题就有迹
# 可循了
################################################
count = [0 for _ in range(26)]  # 统计每个字符出现的次数
s = ''  # 定义一个用于存储字符串的变量
for i in range(4):  # 录入每一行的字符串
    s = s + input()
for j in s:  # 遍历每一个字符
    if 'A' <= j <= 'Z':
        count[ord(j) - ord('A')] += 1

peak = max(count)  # 记录当前出现最大次数的字符串
for i in range(peak):  # 设定打印范围(行)
    for j in range(26):
        if count[j] == peak:  # 如果某字符出现的个数等于peak
            print("*", end="")
            count[j] -= 1
            if max(count) == peak:
                print(" ", end="")
        else:
            if max(count) == peak:
                print(" ", end=" ")
    print()
    peak -= 1

for i in range(26):
    if i != 25:
        print(chr(i + ord('A')), end=" ")
    else:
        print(chr(i + ord('A')), end="")
