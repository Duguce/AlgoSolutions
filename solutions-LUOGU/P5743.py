# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/4 8:36
# @File    : P5743.py
# @Software: PyCharm
n = int(input())
ans = 1
for i in range(1, n):  # 猴子一共吃了n-1天
    ans = ans + 1
    ans = 2 * ans
print(ans)
