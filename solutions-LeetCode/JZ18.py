# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/19 17:19
# @File    : JZ18.py
# @Software: PyCharm
################################################
# hint
# 面试题18：删除链表节点
################################################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        while pre.next and pre.next.val != val:
            pre = pre.next
        if pre.next:
            pre.next = pre.next.next
        return head


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    sol = Solution()
    head = sol.deleteNode(head, 5)

    while head:
        print(head.val, end=" ")
        head = head.next
