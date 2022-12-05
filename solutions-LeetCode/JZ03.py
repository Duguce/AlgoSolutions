# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/5 14:32
# @File    : JZ03.py
# @Software: PyCharm
################################################
# hint
# 面试题3：数组中重复的数字
################################################
from typing import List


class Solution:
    # 方法一：首先，对输入的数组排序。然后，从头到尾扫描排序后的数组找出重复的数字。
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             return nums[i]

    # 方法二：哈希表
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     dic = {}
    #     for n in nums:
    #         if n not in dic:
    #             dic[n] = 1
    #         else:
    #             return n

    # 方法三：类似原地哈希表
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # 注意二者的顺序不能颠倒


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
