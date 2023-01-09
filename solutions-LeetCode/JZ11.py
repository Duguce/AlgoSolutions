# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/9 10:54
# @File    : JZ11.py
# @Software: PyCharm
################################################
# hint
# 面试题11：旋转数组的最小数字
################################################
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1

        return numbers[left]


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    sol = Solution()
    print(sol.minArray([3, 4, 5, 1, 2]))
