# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/12 20:30
# @File    : JZ12.py
# @Software: PyCharm
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) if board else 0

        def dfs(k, i, j):
            if not 0 <= i < m or not 0 <= j < n or word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(k + 1, i - 1, j) or dfs(k + 1, i + 1, j) or dfs(k + 1, i, j - 1) or dfs(k + 1, i, j + 1)
            board[i][j] = tmp
            return res

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True

        return False


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    sol = Solution()
    print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
