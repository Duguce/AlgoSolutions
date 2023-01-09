# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/31 21:58
# @File    : JZ06.py
# @Software: PyCharm
################################################
# hint
# 面试题6：从尾到头打印链表
################################################
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法一：递归法
    # def reversePrint(self, head: ListNode) -> List[int]:
    #     return self.reversePrint(head.next) + [head.val] if head else []

    # 方法二：辅助栈法
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    head = [1, 3, 2]
    list_node = ListNode(head)
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(2)
    l1.next = l2
    l2.next = l3
    l3.next = None

    sol = Solution()
    print(sol.reversePrint(l1))
