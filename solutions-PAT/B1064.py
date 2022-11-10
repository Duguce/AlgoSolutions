# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/9 7:57
# @File    : B1064.py
# @Software: PyCharm
################################################
# hint
# 朋友数
################################################
def func():
    n = int(input())
    lst = list(input().split())
    ans = []  # 用以记录朋友数
    for l in lst:
        l = sum(map(int, list(l)))
        if l not in ans:
            ans.append(l)
    ans.sort()  # 朋友数按照递增排序
    print(len(ans))
    print(*ans, sep=" ")


if __name__ == '__main__':
    func()
