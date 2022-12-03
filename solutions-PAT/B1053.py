# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/3 8:47
# @File    : B1053.py
# @Software: PyCharm
################################################
# hint
# 住房空置率
################################################
def func():
    lst = input().split()
    N, e, D = int(lst[0]), float(lst[1]), int(lst[2])
    poss_vacant = 0
    vacant = 0
    for _ in range(N):
        h_num, *house_lst = map(float, input().split())
        each_count = 0
        for h in house_lst:
            if h < e:
                each_count += 1
        if each_count > h_num / 2 and h_num > D:
            vacant += 1
        elif each_count > h_num / 2:
            poss_vacant += 1

    print("{0:.1%} {1:.1%}".format(poss_vacant / N, vacant / N))


if __name__ == '__main__':
    func()
