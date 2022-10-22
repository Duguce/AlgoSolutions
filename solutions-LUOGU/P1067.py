# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/18 8:10
# @File    : P1067.py
# @Software: PyCharm
################################################
# hint
# 多项式模拟，需要注意细节
################################################
def func():
    n = int(input())
    fac_arr = list(map(int, input().strip().split()))

    pol = ""
    for i, e in enumerate(fac_arr):
        if e != 0:  # 系数不为零时
            if e == 1 and i != n:  # 当系数为1且不为最后一项
                e = ""
            if e == -1 and i != n:  # 当系数为-1且不为最后一项
                e = "-"

            if i == n:  # 当为最后一项时
                pol += f"{e}+"
            elif i == n - 1:
                pol += f"{e}x+"
            else:
                pol += f"{e}x^{n - i}+"

    print(pol[:-1].replace("+-", "-"))


if __name__ == '__main__':
    func()
