# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/24 12:30
# @File    : JZ19.py
# @Software: PyCharm
################################################
# hint
# 面试题19：正则表达式匹配
################################################
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') if p[
                                                                                                             j - 1] == '*' else \
                    dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.isMatch('aa', 'a'))
    # --------------------测试用例2-------------------- #
    sol = Solution()
    print(sol.isMatch('aaa', 'a*'))
