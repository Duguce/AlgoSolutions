# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/20 17:55
# @File    : P1957.py
# @Software: PyCharm
n = int(input())
list = []
op = '+'
ans = 0
for i in range(n):
    list.append(input().split())
for arr in list:
    if len(arr) == 3:
        if arr[0] == 'a':
            op = '+'
        elif arr[0] == 'b':
            op = '-'
        elif arr[0] == 'c':
            op = '*'
        ans = arr[1] + op + arr[2]  # 列出运算式
        print("{}{}{}={}".format(arr[1], op, arr[2], eval(ans)))  # eval函数执行了eval中的运算式
    else:
        ans = arr[0] + op + arr[1]
        print("{}{}{}={}".format(arr[0], op, arr[1], eval(ans)))
    print(len(ans) + 1 + len(str(eval(ans))))
print(len(ans))
