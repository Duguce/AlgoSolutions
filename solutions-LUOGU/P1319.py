# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/19 20:12
# @File    : P1319.py
# @Software: PyCharm
################################################
# hint
# 两次模拟，总体思路不麻烦，注意细节
################################################
arr = list(map(int, input().split()))
k = 1
temp = arr[k]  # 用于记录当前数需要打印的次数
for i in range(arr[0]):  # 控制行数
    for j in range(arr[0]):  # 控制列数
        if temp == 0 and k < len(arr) - 1:  # 当前数需要打印的次数，且k不超过数组的长度
            k += 1  # 当前数打印完之后
            temp = arr[k]  # 打印下一个值
        if k % 2 != 0:  # 判断当前值是打印0，还是1
            print(0, end='')
        else:
            print(1, end='')
        temp -= 1
    print()  # 换行
