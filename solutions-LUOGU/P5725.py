# -*- coding: utf-8  -*-
################################################
# hint
# 本题是一个打印正方形和三角形的问题。我的方法很简单，用双
# 层循环打印一下即可（外层控制行数，内层控制打印数字）
# 需要特别注意的是：打印三角形的时候，每一次打印的空格是
# 两个空格字符，以及数字补零的问题。
################################################
n = int(input())
num1 = 0
num2 = 0
# 打印正方形矩阵
for i in range(1, n + 1):
    for j in range(1, n + 1):
        num1 += 1
        print(str(num1).rjust(2, '0'), end='')
    print()
print()
# 打印三角形矩阵
for i in range(1, n + 1):
    s = n - i
    for j in range(s):
        print('  ', end='')
    while i > 0:
        num2 += 1
        print(str(num2).rjust(2, '0'), end='')
        i -= 1
    print()
