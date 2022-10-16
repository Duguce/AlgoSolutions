# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/12 8:56
# @File    : P2415.py
# @Software: PyCharm
################################################
# hint
# 本题要求对集合的子集进行求和，关键点在于明白集合的每一
# 个元素在所有子集中出现的次数，分析后发现每个元素都出现
# 了2**(n-1)次。
################################################
def func():
    s = list(map(int, input().split()))
    ans = 0
    n = len(s)
    for i in s:
        ans += i * (2 ** (n - 1))
    print(ans)


if __name__ == '__main__':
    func()
