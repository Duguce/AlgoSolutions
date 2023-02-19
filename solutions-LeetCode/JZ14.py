# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/13 12:08
# @File    : JZ14.py
# @Software: PyCharm
################################################
# hint
# 面试题14：剪绳子
################################################
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * max(dp[i - j], i - j))
        return dp[n]


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.cuttingRope(2))
    # --------------------测试用例2-------------------- #
    sol = Solution()
    print(sol.cuttingRope(10))
