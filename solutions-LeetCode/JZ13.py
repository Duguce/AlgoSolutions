# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/18 20:49
# @File    : JZ13.py
# @Software: PyCharm
################################################
# hint
# 面试题13：机器人的运动范围
################################################
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def getDigitSum(i, j):
            res = 0
            while i:
                res += i % 10
                i //= 10
            while j:
                res += j % 10
                j //= 10
            return res

        visited = set()

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or getDigitSum(i, j) > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.movingCount(2, 3, 1))
    # --------------------测试用例2-------------------- #
    sol = Solution()
    print(sol.movingCount(3, 1, 0))
