# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/14 11:36
# @File    : JZ15.py
# @Software: PyCharm
################################################
# hint
# 面试题15：二进制中1的个数
################################################
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1

        return res


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.hammingWeight(11))
