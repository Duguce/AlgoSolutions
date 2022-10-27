# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/26 18:29
# @File    : P1059.py
# @Software: PyCharm
################################################
# hint
# 明明的随机数：排序
################################################
def func():
    n = int(input())
    lst = list(map(int, input().split()))
    ans = []
    for l in lst:
        if l not in ans:
            ans.append(l)

    print(len(ans))
    print(*sorted(ans), sep=" ")


if __name__ == '__main__':
    func()
