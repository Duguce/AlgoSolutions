# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/7 10:09
# @File    : JZ04.py
# @Software: PyCharm
################################################
# hint
# 面试题4：二维数组中的查找
################################################
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    sol = Solution()
    print(sol.findNumberIn2DArray([[1, 4, 7, 11, 15],
                                   [2, 5, 8, 12, 19],
                                   [3, 6, 9, 16, 22],
                                   [10, 13, 14, 17, 24],
                                   [18, 21, 23, 26, 30]
                                   ], 20))
