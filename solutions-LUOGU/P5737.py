# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/3 9:31
# @File    : P5737.py
# @Software: PyCharm
################################################
# hint
# 本题的核心是判断闰年，就不多说啦
################################################
def isLeapYear(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    return False


start, end = map(int, input().split())  # 输入起止年份
count = 0  # 计算区间内出现闰年的个数
leapYear = []  # 用于存储区间内是闰年的年份
for i in range(start, end + 1):
    if isLeapYear(i):
        count += 1
        leapYear.append(i)

print(count)
print(*leapYear, sep=" ", end="")
