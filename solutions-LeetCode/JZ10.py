# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/8 19:06
# @File    : JZ10.py
# @Software: PyCharm
################################################
# hint
# 面试题10：青蛙跳台阶问题
################################################
class Solution:
    def numWays(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(n):
            x, y = y, x+y
        return x % 1000000007
