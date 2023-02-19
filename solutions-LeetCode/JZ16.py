# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/15 10:17
# @File    : JZ16.py
# @Software: PyCharm
################################################
# hint
# 面试题16：数值的整数次方
################################################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.myPow(2.00000, 10))
    # --------------------测试用例2-------------------- #
    sol = Solution()
    print(sol.myPow(2.10000, 3))
