# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/3 17:47
# @File    : P1923.py
# @Software: PyCharm
################################################
# hint
# 求第k小的数：注意不能直接排序查找（部分测试点内存会爆）
# 这里借助numpy库来优化一下
################################################
import numpy as np


def func():
    n, k = map(int, input().split())
    lst = np.fromstring(input(), dtype=np.uint32, sep=" ")
    lst.sort()
    min_k = lst[k]
    print(min_k)


if __name__ == '__main__':
    func()
