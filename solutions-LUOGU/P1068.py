# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/3 8:47
# @File    : P1068.py
# @Software: PyCharm
################################################
# hint
# 分数线划分：注意可能有多个人卡在分数线上
################################################
def func():
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    last = int(m * 1.5) - 1  # 进入面试的分数线对应的选手索引
    lst = sorted(lst, key=lambda l: (l[1], -l[0]), reverse=True)  # 对通过笔试的选手进行排序
    volunteers = []  # 记录进入面试人员的信息
    for i in range(n):
        if lst[i][1] >= lst[last][1]:
            volunteers.append(lst[i])
        else:
            break
    print(volunteers[last][1], len(volunteers))
    for v in volunteers:
        print(*v, sep=" ")


if __name__ == '__main__':
    func()
