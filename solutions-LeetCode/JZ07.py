# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/5 20:43
# @File    : JZ07.py
# @Software: PyCharm
################################################
# hint
# 面试题7：重建二叉树
################################################
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {val: i for i, val in enumerate(inorder)}

        def construct(preRootId, inL, inR):
            if inL > inR:
                return None
            rootVal = preorder[preRootId]
            inRootId = index[rootVal]
            leftSize = inRootId - inL
            root = TreeNode(rootVal)
            root.left = construct(preRootId + 1, inL, inRootId - 1)
            root.right = construct(preRootId + leftSize + 1, inRootId + 1, inR)
            return root

        return construct(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    sol.buildTree(preorder, inorder)
