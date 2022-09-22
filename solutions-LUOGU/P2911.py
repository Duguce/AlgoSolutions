# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/16 16:43
# @File    : P2911.py
# @Software: PyCharm
################################################
# hint
# 审题审题，要求输出的是和的最大值！不是对应的次数!
################################################
s1, s2, s3 = map(int, input().split())  # 三个骰子的面数
ans = 0
ansArr = [0] * (s1 + s2 + s3 + 1)  # 定义一个数组用于记录每一种和出现的次数
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            ansArr[i + j + k] += 1

for i in range(len(ansArr)):
    if ansArr[i] > ansArr[ans]:
        ans = i
print(ans)
