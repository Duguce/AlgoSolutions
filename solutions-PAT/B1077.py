# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/9 21:20
# @File    : B1077.py
# @Software: PyCharm
################################################
# hint
# 互评成绩计算
################################################
def func():
    n, m = map(int, input().split())
    lst = [[i for i in map(int, input().split()) if 0 <= i <= m] for _ in range(n)]

    for l in lst:
        g1 = l[0]
        g2 = (sum(l[1:]) - max(l[1:]) - min(l[1:])) / (len(l) - 3)
        score = int((g1 + g2) / 2 + 0.5)  # 对分数进行四舍五入取整
        print(score)


if __name__ == '__main__':
    func()
