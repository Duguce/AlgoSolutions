# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/4 9:02
# @File    : P2089.py
# @Software: PyCharm
################################################
# hint
# 烤鸡：暴力搜索
################################################
def func():
    n = int(input())
    ans = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    for e in range(1, 4):
                        for f in range(1, 4):
                            for g in range(1, 4):
                                for h in range(1, 4):
                                    for i in range(1, 4):
                                        for j in range(1, 4):
                                            if a + b + c + d + e + f + g + h + i + j == n:
                                                ans.append([a, b, c, d, e, f, g, h, i, j])

    print(len(ans))
    for l in ans:
        print(*l, sep=" ")


if __name__ == '__main__':
    func()
