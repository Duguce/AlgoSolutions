# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/27 10:52
# @File    : B1070.py
# @Software: PyCharm
################################################
# hint
# 结绳
################################################
def func():
    n = int(input())
    lst = sorted(map(int, input().split()))
    ans = lst[0]
    for i in range(1, n):
        ans = int((ans + lst[i]) / 2)
    print(ans)


if __name__ == '__main__':
    func()
